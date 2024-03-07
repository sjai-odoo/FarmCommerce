# -*- coding: utf-8 -*-
from odoo import http, fields
import math

class Farming(http.Controller):
    
    @http.route(['/farm'], auth='public', website=True)
    def index(self, page=1, **kw):
        vegetables = http.request.env['product.property'].search([('pro_category', '=', 'vegetables')]) # offset willskip that much properties in the beginning
        grains = http.request.env['product.property'].search([('pro_category', '=', 'grains')]) # offset willskip that much properties in the beginning
        return http.request.render('Farming.index', { 
            'vege_records': vegetables,
            'grain_records': grains,
        })# here the real-estate is our module.id of the template

    @http.route(['/farm/Coconut'], auth='public', website=True)
    def index(self, page=1, **kw):
        vegetables = http.request.env['product.property'].search([('name', '=', 'Coconut')]) # offset willskip that much properties in the beginning
        return http.request.render('Farming.hey', { 
            'vege_records': vegetables,
        })# here the real-estate is our module.id of the template
    
    