# -*- coding: utf-8 -*-
# from odoo import http


# class ShopifyPostProcessing(http.Controller):
#     @http.route('/shopify_post_processing/shopify_post_processing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shopify_post_processing/shopify_post_processing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('shopify_post_processing.listing', {
#             'root': '/shopify_post_processing/shopify_post_processing',
#             'objects': http.request.env['shopify_post_processing.shopify_post_processing'].search([]),
#         })

#     @http.route('/shopify_post_processing/shopify_post_processing/objects/<model("shopify_post_processing.shopify_post_processing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shopify_post_processing.object', {
#             'object': obj
#         })
