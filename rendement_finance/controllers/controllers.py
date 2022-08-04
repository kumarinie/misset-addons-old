# -*- coding: utf-8 -*-
from odoo import http

# class RendementFinance(http.Controller):
#     @http.route('/rendement_finance/rendement_finance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rendement_finance/rendement_finance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rendement_finance.listing', {
#             'root': '/rendement_finance/rendement_finance',
#             'objects': http.request.env['rendement_finance.rendement_finance'].search([]),
#         })

#     @http.route('/rendement_finance/rendement_finance/objects/<model("rendement_finance.rendement_finance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rendement_finance.object', {
#             'object': obj
#         })