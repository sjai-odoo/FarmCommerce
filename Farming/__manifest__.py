#-- coding: utf-8 --
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Farm_Commerce',
    'description': 'It will serve as a platform for the targeted lower economic farmers to directly sale their ingradients to customers and improve the margin which help them to sustain',
    'summary': 'A try to help the farmers grow economically',
    'category' : 'users/contact type',
    'installable': True,
    'application': True,
    'depends': ['base'],
    'license': 'OEEL-1',
    'version': '1.0',
    'data' : [
        'security/users.xml',
        'security/ir.model.access.csv',
        'views/contact_views.xml',
    ]
}
