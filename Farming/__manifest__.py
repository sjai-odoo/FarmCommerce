#-- coding: utf-8 --
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'farm_commerce',
    'description': 'It will serve as a platform for the targeted lower economic farmers to directly sale their ingradients to customers and improve the margin which help them to sustain',
    'summary': 'A try to help the farmers grow economically',
    'category' : 'users/contact type',
    'installable': True,
    'application': True,
    'depends': ['base','website'],
    'license': 'OEEL-1',
    'sequence': 1,
    'version': '1.0',
    'data' : [
        'security/users.xml',
        'security/ir.model.access.csv',
        'data/website_data.xml',
        'views/farming_templates.xml',
        'views/contact_views.xml',
        'views/product_views.xml',
        'views/order_lines_views.xml',
        'views/cart_items_views.xml',
        'views/menuitems.xml',
    ]
}
