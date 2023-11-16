# -*- coding: utf-8 -*-
{
    'name': "shopify_post_processing",

    'summary': """
        Shopify Post Processing""",

    'description': """
        Shopify Post Processing
    """,

    'author': "TOSC",
    'website': "http://www.tosc.nl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_advertising_order'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'demo/cron_data.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
