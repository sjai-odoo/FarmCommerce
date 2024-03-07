#-- coding: utf-8 --
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'farm_account',
    'description': 'It will serve as a platform for the targeted lower economic farmers to directly sale their ingradients to customers and improve the margin which help them to sustain',
    'summary': 'A try to help the farmers grow economically',
    'installable': True,
    'application': True,
    'depends': ['Farming','account_accountant'],
    'license': 'OEEL-1',
    'version': '1.0',
    'auto_install': True, # automatically install this module if all dependecies are installed
    'data' : [
        'report/farm_commerce_reports.xml',
        'report/farm_commerce_templates.xml',
        'views/contact_views.xml',
        'views/product_views.xml'
    ]
}
