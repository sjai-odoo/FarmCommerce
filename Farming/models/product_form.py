from odoo import fields, models , exceptions , api

class ProductProperty(models.Model):
    _name = 'product.property'
    _description = 'Product Details'

    color = fields.Integer(string='Color')
    cost = fields.Float('Cost per unit')
    farmer_ids = fields.Many2many('contact.property')
    name = fields.Char(string='Product Name', required = True, size = 20)
    order_line_id = fields.Many2one('sale.order.line')
    pro_category = fields.Selection(string='Category', selection=[('grains','Grains'),('vegetables','Vegetables')])
    pro_image = fields.Image(string='Image', max_height = 500, max_width = 500)
    quantity = fields.Float('Quantity (in kg)')
    sales_price = fields.Float('Selling Price')  
    tax = fields.Selection(string='Tax', selection=[( '5','5% tax'),( '15', 'Base 15%'),( '21', '21% tax')])
