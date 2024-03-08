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

        return http.request.render('Farming.product_page', { 
            'product': product,
            'name': name,
        })

    @http.route(['/products/cart/<name>'], type='http', auth='public', website=True)
    def cart(self, name, quantity, page=1, **post):
        # Retrieve cart_products dictionary from session or create an empty one
        cart_products = request.session.get('cart_products', {'orders': []})

        breakpoint()
        cart_products['orders'].append({'name': name, 'quantity': quantity})
        print(cart_products,"------------------------------------------------------")
        # Update cart_products in user session
        request.session['cart_products'] = cart_products
        print(cart_products,"--------------------------------------------------------")
        
        return http.request.render('Farming.cart', {
            'cart_products': cart_products['orders'],
        })

    @http.route(['/products/cart'], type='http', auth='public', website=True)
    def view_cart(self, **kw):
        # Retrieve cart_products dictionary from session or create an empty one
        cart_products = request.session.get('cart_products', {'orders': []})

        return http.request.render('Farming.cart', {
            'cart_products': cart_products['orders'],
        })