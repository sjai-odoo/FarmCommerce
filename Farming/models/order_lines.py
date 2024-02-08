from odoo import fields, models , exceptions , api

TAXES = [
    ( 5,'5% tax'),
    ( 15, 'Base 15%'),
    ( 21, '21% tax'),
]

class SaleOrderLine(models.Model):
    _name = 'sale.order.line'
    _description = "Sales Order Line"
    _order = 'order_id, sequence, id'

    # fields

    product_id = fields.Many2one(
        comodel_name='product.property',
        string="Product",
        change_default=True, ondelete='restrict', 
        index='btree_not_null', #because product-id should not be null
    )

    name = fields.Text(
        string="Description",
        compute='_compute_name',
        related='product.property.name',
        store=True, readonly=False, required=True
    )

    description = fields.Text(
        string="Description",
        store=True, readonly=False,
    )

    price_unit = fields.Float(
        string="Unit Price",
        related='product.property.sale_price',
        store=True, readonly=False, required=True, precompute=True
    )

    quantity = fields.Integer(
        string="Qty",
        store=True, readonly=False, required=True,
    )

    tax = fields.Selection(
        string="Taxes", related='product.property.tax',
        selection=TAXES, default=5
    ) # tax to apply should be for every product

    tax_amount = fields.Float(string="Total Tax",store=True, readonly=True, compute='_compute_total')# Total tax amount 
    amount_total = fields.Monetary(string="Total", store=True, compute='_compute_total') # total billed amount


    # Methods
    @api.depends('price_unit','tax')
    def _compute_total(self):
        bill_total=0
        without_tax_total=0
        for record in self:
            without_tax_total+=record.quantity*record.price_unit
            bill_total+=record.quantity*(record.price_unit*(1+(record.tax/100)))
        # self.amount_total = bill_total
        # self.tax_amount = self.amount_total - self.without_tax_total
        # can't update like this bcz this fields will be for every records in the table so we can't do like this we need one global 
    
        