# Part of Odoo. See LICENSE file for full copyright and licensing details.
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) PySquad Informatics (<https://www.pysquad.com/>).
#
#    For Module Support : solutions@pysquad.com
#
##############################################################################

{
# Module Info
    'name': 'Sale Price Control',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'license': 'AGPL-3',
    'summary': """
        This module lets you set a minimum sale price per product based on user groups.
        Users cannot confirm a Sale Order if a product is priced below the allowed minimum, and the system shows a clear warning to prevent losses or unauthorized discounts.
    """,
    'description': """
        Sale Price Control & Minimum Price Rule.
        Minimum Sale Price Restriction,
        Sale Order Price Guard,
        Sale Price Protection,
        Minimum Selling Price Manager,
        sale price control,
        minimum sale price,
        price restriction odoo,
        sale order price warning,
        product minimum price,
        prevent low sale price,
        odoo price guard,
        discount restriction odoo,
        sale approval price limit,
    """,

    # Author
    'author': 'Pysquad Informatics',
    'website': 'https://pysquad.com/odoo-erp',

    # Dependencies
    'depends': ['base', 'sale_management'],

    # Data File
    'data': [
        'security/groups.xml',
        'views/product_template_view.xml',
        'views/sale_order_view.xml',
        'views/res_config_settings_view.xml',
    ],
    'images': [
        'static/description/banner_img.png',
    ],

    # Technical Info.
    'application': True,
    'installable': True,
    'auto_install': False,
}