# -*- coding: utf-8 -*-
{
    'name': "rendement_finance",

    'summary': """
        Defining analytic accounting object from invoice line
        & display in list view""",

    'description': """
        Defining analytic accounting object from invoice line
    """,

    'author': "K.Sushma",
    'website': "http://www.tosc.nl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account', 'analytic'],

    # always loaded
    'data': [
        'security/security_view.xml',
        'views/account_invoice_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}