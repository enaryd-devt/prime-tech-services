from odoo import models, fields

class PosConfig(models.Model):
    _inherit = "pos.config"

    default_partner_id = fields.Many2one(
        "res.partner",
        string="Client par défaut",
        help="Client automatiquement sélectionné dans le POS"
    )
