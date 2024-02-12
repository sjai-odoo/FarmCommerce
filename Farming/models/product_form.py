from odoo import fields, models , exceptions , api

# TAXES = [
#     ( 5,'5% tax'),
#     ( 15, 'Base 15%'),
#     ( 21, '21% tax'),
# ]

PRODUCT_TYPES = [
    ( 'consumable','Consumable'),
    ( 'service','Service'),
    ( 'storable','Storable Product'),
]

class ProductProperty(models.Model):
    _name = "product.property"
    _description = "Product Details"

    pro_name = fields.Char(
        string='Product Name', 
        required = True, size = 20) # The name should contain less than 20 char
    
    pro_image = fields.Image(
        string='Image', 
        max_height = 500, max_width = 500) # make it in a way to accept only jpg and png
    
    can_be_sold = fields.Boolean(
        string='Can be Sold', default=True)
    
    can_be_purchased = fields.Boolean(
        string='Can be Purchased', default=True)
    
    # product_uom = fields.Many2one(
    #     'uom.uom', 'Unit of Measure',
    #     related='product_tmpl_id.uom_po_id')

    pro_type = fields.Selection(
        string='Product Type',
        selection=PRODUCT_TYPES, default='consumable')

    saler_name = fields.Char(
        string='Saler', ) # only for b2b in b2c every product will be sold anonymously 
        # related='contact.property.name'
    
    pro_category = fields.Selection(
        string='Category',
        selection=[('grains',"Grains"),('vegetables','Vegetables')])

    quantity = fields.Float('Quantity (in kg)')
    sales_price = fields.Float('Selling Price')
    cost = fields.Float('Cost per unit')
    buyer = fields.Selection(selection=[('b2b','B2B'),('b2c','B2C')])
    tax = fields.Selection(string='Tax', selection=[( '5','5% tax'),( '15', 'Base 15%'),( '21', '21% tax')])
