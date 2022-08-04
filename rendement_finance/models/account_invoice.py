# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Invoice(models.Model):
    _inherit = 'account.invoice'

    @api.depends('invoice_line_ids')
    @api.multi
    def _compute_line_analytic(self):
        for rec in self:
            if rec.type in ('in_invoice', 'in_refund'):
                account_analytic_id = rec.invoice_line_ids.mapped('account_analytic_id')
                rec.line_account_analytic_id = account_analytic_id and account_analytic_id.ids[0] or False
            else:
                rec.line_account_analytic_id = False

    line_account_analytic_id = fields.Many2one('account.analytic.account', 'Analytic account', compute=_compute_line_analytic)
