from odoo import fields, models , exceptions , api
from odoo.exceptions import ValidationError

class PurchaseOrderLine(models.Model):
    _name = 'purchase.order.line'
    _inherit = 'sale.order.line'

    purchase_id = fields.Many2one('contact.property', string='Buyers')
    price_unit = fields.Float()
    
    @api.depends('name')
    def _set_price(self):
        for record in self:
            req_product = record.product_ids.filtered(lambda product : product.name == self.name)
            record.price_unit = req_product.cost
