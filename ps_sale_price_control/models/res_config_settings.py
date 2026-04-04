from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    enable_sale_minimum_price = fields.Boolean(string="Sale Minimum Price", store=True,
                                               config_parameter="ps_sale_price_control.enable_sale_minimum_price")
