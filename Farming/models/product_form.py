from odoo import fields, models , exceptions , api

class ProductProperty(models.Model):
    _name = 'product.property'
    _description = 'Product Details'

    name = fields.Char(string='Product Name', required = True, size = 20) # The name should contain less than 20 char
    order_line_id = fields.Many2one('sale.order.line')
    pro_image = fields.Image(string='Image', max_height = 500, max_width = 500) # make it in a way to accept only jpg and png
    quantity = fields.Float('Quantity (in kg)')
    sales_price = fields.Float('Selling Price') # add this in contact form itself this is our fixed selling price    
    pro_category = fields.Selection(string='Category', selection=[('grains','Grains'),('vegetables','Vegetables')])
    quantity = fields.Float('Quantity (in kg)') # should be sum of all parteners quantities
    sales_price = fields.Float('Selling Price')
    cost = fields.Float('Cost per unit')
    tax = fields.Selection(string='Tax', selection=[( '5','5% tax'),( '15', 'Base 15%'),( '21', '21% tax')])
    color = fields.Integer(string='Color')
    farmer_ids = fields.Many2many('contact.property', )
