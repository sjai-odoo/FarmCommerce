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
        uid = http.request.env.user.id
        existing_item = request.env['cart.item'].sudo().search([('create_uid','=',uid)]).filtered(lambda item: item.product_id.id == int(product_id)) #existing item if exist
        breakpoint()
        # items already in cart add quantity
        if len(existing_item)>0:
            existing_item.quantity += int(quantity)

        else: #create if not already in cart
            cart_item = request.env['cart.item'].sudo().create({
                'product_id': int(product_id),
                'quantity': int(quantity),
            })

        return request.redirect('/cart')

    @http.route('/cart/minus/<int:product_id>', type='http', auth='public', website=True)
    def edit_cart(self, product_id, **post):
        uid = http.request.env.user.id
        cart_items = request.env['cart.item'].sudo().search([('create_uid','=',uid),('state','=','draft')]) #all items
        for i in cart_items:
            if (i.product_id.id == product_id):
                i.quantity-=1
        return request.redirect('/cart')

    @http.route(['/cart/delete/<int:item_id>'], auth="public", website=True)
    def delete_item(self, item_id, **post):
        uid = http.request.env.user.id
        cart_items = request.env['cart.item'].sudo().search([('create_uid','=',uid),('state','=','draft')]) #all items
        record_to_delete = cart_items.sudo().search([('id','=',item_id)])
        record_to_delete.unlink()
        return request.redirect('/cart')
    
    @http.route(['/cart/delete/'], auth="public", website=True)
    def delete_all(self, **post):
        uid = http.request.env.user.id
        cart_items = request.env['cart.item'].sudo().search([('create_uid','=',uid)]) #all items
        for item in cart_items:
            item.state='ordered'
        return request.redirect('/cart')

    @http.route('/cart', type='http', auth='public', website=True)
    def view_cart(self, **post):
        uid = http.request.env.user.id
        uimage = http.request.env.user.image_1920
        user_cart_items = request.env['cart.item'].sudo().search([('create_uid','=',uid),('state','=','draft')]) #user's cart

        total_billing_amount=0
        for item in user_cart_items:
            total_billing_amount += (item.quantity*item.product_id.cost)
        
        return http.request.render('Farming.view_cart', {
            'user_image': uimage,
            'cart_item_numbers': len(user_cart_items),
            'users_cart': user_cart_items,
            'total_amount': total_billing_amount,
        })
