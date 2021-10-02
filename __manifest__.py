# -*- coding: utf-8 -*-
{
    'name': "Document Management",

    'summary': """""",

    'description': """
    """,

    'author': "Frank Alwis",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'sale_management', 'account', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/document_management_groups.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/sale_order_views.xml',
        'wizards/document_rejection_views.xml',
        'views/document_management_views.xml',
        'views/document_management_menu.xml',
        'views/account_invoice_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
