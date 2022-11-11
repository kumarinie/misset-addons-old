from odoo import api, fields, models, _


class productTemplate(models.Model):
    _inherit = "product.template"

    price_fixed = fields.Boolean(
        'Price Fixed',
        help="Price Fixed for expense per kilometer")