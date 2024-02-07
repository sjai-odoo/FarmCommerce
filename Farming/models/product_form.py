from odoo import fields, models , exceptions , api

class ProductProperty(models.Model):
    _name = "product_property"
    _description = "Product Details"

    pro_name = fields.Char('Name', required=True, size=20) # The name should contain less than 20 char
    saler_name = fields.Char('Saler') # only for b2b in b2c every product will be sold anonymously 
    quantity = fields.Float('Quantity (in kg)')
    sale_price = fields.Float('Selling Price', required=True)
    buyer = fields.Selection(selection=[('b2b','B2B'),('b2c','B2C')])
    pro_category =fields.Selection(String='Category',selection=[('grains',"Grains"),('vegetables','Vegetables')])
    