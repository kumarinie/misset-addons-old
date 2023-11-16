# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Sale(models.Model):
    _inherit = 'sale.order'

    @api.model
    def run_order_operating_unit_updates(self):
        saleObj = self.search([('state', '=', 'sale'),('company_id.id', '=', 2)])
        saleObj.write({'operating_unit_id':2})

    @api.model
    def run_sale_order_make_invoices(self):
        saleObj = self.search([('state', '=', 'sale'), ('company_id.id', '=', 2), ('operating_unit_id.id', '=', 2)])
        if saleObj:
            wizard = self.env['ad.order.make.invoice'].create({'job_queue':True})
            wizard.with_context({'active_ids': saleObj.ids}).make_invoices_from_ad_orders()
