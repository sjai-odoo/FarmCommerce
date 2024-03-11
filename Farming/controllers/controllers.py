# -*- coding: utf-8 -*-
from odoo import http, fields
import math
from odoo.http import request

class Farming(http.Controller):
    
    @http.route(['/products'], auth="public", website=True)
    def index(self, page=1, **kw):
        products = http.request.env['product.property'].search([])
        return http.request.render('Farming.index', { 
            'products': products,
        })
    
    @http.route(['/products/<name>/'], auth="public", website=True)
    def product_page(self, name, **post):
        product = http.request.env['product.property'].search([('name', '=', name)])
        products = http.request.env['product.property'].search([])

        return http.request.render('Farming.product_page', { 
            'product': product,
            'name': name,
        })

    @http.route('/add_to_cart', type='http', auth='public', website=True)
    def add_to_cart(self, product_id, quantity, **post):
        cart_item = request.env['cart.item'].sudo().create({
            'product_id': product_id,
            'quantity': quantity,
        })
        return request.redirect('/cart')

    @http.route('/cart', type='http', auth='public', website=True)
    def view_cart(self, **post):
        cart_items = request.env['cart.item'].sudo().search([])
        return http.request.render('Farming.view_cart', {
            'cart_items': cart_items,
        })
