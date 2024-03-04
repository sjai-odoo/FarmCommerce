from odoo import fields, models , exceptions , api
from odoo.exceptions import ValidationError

class SaleOrderLine(models.Model):
    _name = 'order.line'
    _description = 'Sales Order Line'

    # fields
    amount_total = fields.Float(string='Total', store=True, compute='_compute_total') # total billed amount
    name = fields.Many2one('product.property')
    price_unit = fields.Float(string='Unit Price', store=True, readonly=False)
    buyer_price_unit = fields.Float(string='Unit Price', store=True, compute='_set_price')
    product_ids = fields.One2many('product.property', 'order_line_id', string='Name', readonly=False)
    purchase_id = fields.Many2one('contact.property', string='Purchase', ondelete='restrict', index='btree_not_null')
    quantity = fields.Integer(string='Qty', store=True, readonly=False, required=True)
    sale_id = fields.Many2one('contact.property', string='Farmer', ondelete='restrict', index='btree_not_null')
    tax = fields.Selection(string='Taxes', selection=[( '5','5% tax'), ( '15', 'Base 15%'), ( '21', '21% tax'),], default='5')
    tax_amount = fields.Float(string='Total Tax',store=True, readonly=True, compute='_compute_total')# Total tax amount 

    # Methods
    @api.depends('price_unit','tax','quantity')
    def _compute_total(self):
        bill_total=0
        without_tax_total=0
        for record in self:
            without_tax_total+=record.quantity*record.price_unit
            bill_total+=record.quantity*(record.price_unit*(1+(int(record.tax)/100)))

        self.amount_total = bill_total
        self.tax_amount = bill_total - without_tax_total
        # can't update like this bcz this fields will be for every records in the table so we can't do like this we need one global 
    
    @api.depends('quantity')
    def _set_price(self):
        for record in self:
            product_property = self.env['product.property'].search([('name', '=', record.name.name)])
            if product_property:
                record.buyer_price_unit = product_property.cost

