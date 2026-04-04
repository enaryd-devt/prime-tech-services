from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    minimum_price = fields.Float(string='Minimum Price')
    is_sale_price_control = fields.Boolean(string='IS Sale price control',
                                           compute='_compute_sale_price_control')

    def _compute_sale_price_control(self):
        Param = self.env['ir.config_parameter'].sudo()
        is_sale_price_control_enabled = Param.get_param('ps_sale_price_control.enable_sale_minimum_price') == 'True'

        if is_sale_price_control_enabled:
            self.is_sale_price_control = True
        else:
            self.is_sale_price_control = False
