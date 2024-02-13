from odoo import fields, models , exceptions , api

class ContactProperty(models.Model):
    _name = 'contact.property'
    _description = 'Contact Details'

    name = fields.Char(string = 'Name', required=True, size=20) # The name should contain less than 20 char
    image = fields.Image('Image', max_height=100, max_width=100, copy=False, attachment=True)
    phone = fields.Integer(string = 'Phone No.', required=True)   
    can_be_sold = fields.Boolean(string='Buyer', default=True)
    can_be_purchased = fields.Boolean(string='Farmer', default=True)
    address = fields.Text(string = 'Address')
    language = fields.Selection(selection=[('eng','English'),('guj','Gujarati'),('hi','Hindi')])
    income_certi = fields.Binary(string = 'Income Certificate by gov.') # binary fields accept all files
    email = fields.Text(string = 'Email')
    category = fields.Many2many('product.property', string='Categories')
    offers = fields.One2many('sale.order.line','contact_id')
