from odoo import fields, models , exceptions , api

TAXES = [
    ( 5,'5% tax'),
    ( 15, 'Base 15%'),
    ( 21, '21% tax'),
]

class ProductProperty(models.Model):
    _name = "product.property"
    _description = "Product Details"

    pro_name = fields.Char('Name', required = True, size = 20) # The name should contain less than 20 char
    pro_image = fields.Image('Image', options = {'accepted':'jpg,png'}, max_height = 500, max_width = 500) # make it in a way to accept only jpg and png
    saler_name = fields.Char('Saler',related='contact.property.name') # only for b2b in b2c every product will be sold anonymously 
    quantity = fields.Float('Quantity (in kg)')
    sale_price = fields.Float('Selling Price')
    buyer = fields.Selection(selection=[('b2b','B2B'),('b2c','B2C')])
    pro_category = fields.Selection(String='Category',selection=[('grains',"Grains"),('vegetables','Vegetables')])
    tax = fields.Selection('Tax',selection=TAXES,default=5)
    invoice_amount = fields.Float(compute='_apply_tax' , digits=(13,2))

    @api.depends('sale_price', 'tax')
    def _apply_tax(self):
        self.invoice_amount = self.sale_price * (1+(self.tax/100))
        