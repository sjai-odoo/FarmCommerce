from odoo import fields, models , exceptions , api
from odoo.exceptions import ValidationError

class SaleOrderLine(models.Model):
    _name = 'sale.order.line'
    _description = 'Sales Order Line'

    # fields
    sale_id = fields.Many2one('contact.property', string='Farmer', ondelete='restrict', index='btree_not_null') #because product-id should not be null
    product_ids = fields.One2many('product.property', 'order_line_id', string='Name', readonly=False)
    name = fields.Many2one('product.property')
    price_unit = fields.Float(string='Unit Price', store=True, readonly=False, required=True,)
    quantity = fields.Integer(string='Qty', store=True, readonly=False, required=True,)
    tax = fields.Selection(string='Taxes', selection=[( '5','5% tax'), ( '15', 'Base 15%'), ( '21', '21% tax'),], default='5') # tax to apply should be for every product
    tax_amount = fields.Float(string='Total Tax',store=True, readonly=True, compute='_compute_total')# Total tax amount 
    amount_total = fields.Float(string='Total', store=True, compute='_compute_total') # total billed amount

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
    
    # @api.model_create_multi # formultiple record creation like importing a record file
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         breakpoint()
    #         products_produced = self.env['']
    #         a= self.env['contact.property'].search([(vals.get('name'), 'in', 'product_ids')])
    #         if(vals.name not in vals.contact_id.product_ids.mapped('name')):
    #             raise ValidationError('First add in the products section')
    #     return super().create(vals_list)
