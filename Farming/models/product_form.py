from odoo import fields, models , exceptions , api

class ProductProperty(models.Model):
    _name = "product.property"
    _description = "Product Details"

    pro_name = fields.Char(
        string='Product Name', 
        required = True, size = 20) # The name should contain less than 20 char
    
    pro_image = fields.Image(
        string='Image', 
        max_height = 500, max_width = 500) # make it in a way to accept only jpg and png

    saler_name = fields.Char(
        string='Saler', ) # only for b2b in b2c every product will be sold anonymously 
        # related='contact.property.name' who all are selling this product
    
    pro_category = fields.Many2many('contact.property', string='Product Categories')

    quantity = fields.Float('Quantity (in kg)')
    sales_price = fields.Float('Selling Price') # add this in contact form itself this is our fixed selling price
    tax = fields.Selection(string='Tax', selection=[( '5','5% tax'),( '15', 'Base 15%'),( '21', '21% tax')])
