from odoo import models, fields

class CartItem(models.Model):
    _name = 'cart.item'

    product_id = fields.Many2one('product.property', string='Product', required=True)
    quantity = fields.Integer(string='Quantity', required=True)
    # total = fields.Float(compute="_total_amount", default=0)

    # @api.depends('product_id','quantity')
    # def _total_amount(self):
    #     for record in self:
    #         self.total += (self.quantity*self.product_id.cost)