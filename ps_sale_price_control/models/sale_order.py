from odoo import api, fields, models, _
from odoo.exceptions import UserError


# =====================================================
# SALE ORDER
# =====================================================

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_sale_price_control = fields.Boolean(
        string='Sale Price Control Enabled',
        compute='_compute_sale_price_control',
        store=False
    )

    def _compute_sale_price_control(self):
        Param = self.env['ir.config_parameter'].sudo()
        enabled = Param.get_param(
            'ps_sale_price_control.enable_sale_minimum_price'
        ) == 'True'

        for order in self:
            order.is_sale_price_control = enabled

    def action_confirm(self):
        Param = self.env['ir.config_parameter'].sudo()
        enabled = Param.get_param(
            'ps_sale_price_control.enable_sale_minimum_price'
        ) == 'True'

        if enabled:
            for order in self:
                invalid_lines = []

                for line in order.order_line:
                    if line.price_unit < line.sale_minimum_price:
                        invalid_lines.append(
                            _("• Product: %s — Unit Price: %s, Minimum Price: %s") %
                            (
                                line.product_id.display_name,
                                line.price_unit,
                                line.sale_minimum_price
                            )
                        )

                if invalid_lines:
                    raise UserError(_(
                        "Some order lines have prices below their minimum allowed price:\n\n%s\n\n"
                        "Please correct them before confirming the order."
                    ) % "\n".join(invalid_lines))

        return super().action_confirm()


# =====================================================
# SALE ORDER LINE
# =====================================================

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    sale_minimum_price = fields.Float(
        string='Minimum Price'
    )

    # -----------------------------------------
    # AUTO SET MINIMUM PRICE FROM PRODUCT
    # -----------------------------------------

    @api.onchange('product_id')
    def _onchange_product_id_set_minimum_price(self):
        for line in self:
            if line.product_id:
                line.sale_minimum_price = (
                    line.product_id.product_tmpl_id.minimum_price
                )
            else:
                line.sale_minimum_price = 0.0

    # -----------------------------------------
    # BLOCK PRICE MODIFICATION BELOW MINIMUM
    # -----------------------------------------

    def write(self, vals):
        Param = self.env['ir.config_parameter'].sudo()
        enabled = Param.get_param(
            'ps_sale_price_control.enable_sale_minimum_price'
        ) == 'True'

        if enabled and 'price_unit' in vals:
            for line in self:
                new_price = vals.get('price_unit', line.price_unit)

                if new_price < line.sale_minimum_price:
                    raise UserError(_(
                        "You cannot set a unit price below the minimum price.\n\n"
                        "Product: %s\n"
                        "Minimum Price: %s"
                    ) % (
                        line.product_id.display_name,
                        line.sale_minimum_price
                    ))

        return super().write(vals)
