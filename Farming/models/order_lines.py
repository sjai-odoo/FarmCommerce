from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo import fields, models , exceptions , api
from odoo.exceptions import ValidationError

class SaleOrderLine(models.Model):
    _name = 'order.line'
    _description = 'Sales Order Line'

    # fields
    amount_total = fields.Float(string='Total', store=True, compute='_compute_total') # total billed amount
    contacts_type = fields.Integer(compute="_compute_display_name", store=True) # just to show on gantt view
    deadline = fields.Datetime(required=True, default=datetime.now())
    start_time = fields.Datetime(compute="_compute_start_date", store=True)
    end_date = fields.Datetime(compute="_compute_end_date")
    name = fields.Many2one('product.property')
    price_unit = fields.Float(string='Unit Price', store=True, readonly=False)
    buyer_price_unit = fields.Float(string='Selling Price', store=True, compute='_set_price') # showed to buyer
    product_ids = fields.One2many('product.property', 'order_line_id', string='Name', readonly=False)
    purchase_id = fields.Many2one('contact.property', string='Purchase', ondelete='restrict', index='btree_not_null')
    quantity = fields.Integer(string='Qty', store=True, readonly=False, required=True)
    sale_id = fields.Many2one('contact.property', string='Farmer', ondelete='restrict', index='btree_not_null')
    state = fields.Selection(string='Status', default='draft', copy=False,
            selection=[('draft','Draft'), ('ordered','Ordered')])
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
    
    @api.depends('name')
    def _set_price(self):
        for record in self:
            product_property = self.env['product.property'].search([('name', '=', record.name.name)])
            if product_property:
                record.buyer_price_unit = product_property.cost
            else:
                record.buyer_price_unit = 0
            
    @api.depends('create_date')
    def _compute_end_date(self):
        for record in self:
            if record.sale_id:
                record.end_date = record.create_date + relativedelta(days=record.sale_id.lead_time) #for farmer
            else:
                record.end_date = record.deadline # for seller deadline na 2 divas pahelathi dekhade

    @api.depends('create_date')
    def _compute_start_date(self):
        for record in self:
            if record.sale_id:
                record.start_time = record.create_date #for farmercreate date
            else:
                record.start_time = record.deadline + relativedelta(days=-3) # for seller before 3 days to deadline

    @api.depends('name') # can't add buyer_id and sale_id bcz one is set at a time
    def _compute_display_name(self):
        for record in self:
            if record.purchase_id:
                record.display_name = f"{record.name.name} , Buyer : {record.purchase_id.buyer_id.name}"
                record.contacts_type = 4
            else:
                record.display_name = f"{record.name.name} , Farmer : {record.sale_id.name}"
                record.contacts_type = 3

    @api.onchange('sale_id','purchase_id')
    def _onchange_sale_id(self):
        for record in self:
            if record.state == 'ordered':
                raise ValidationError('You cannot change order line after confirmed.')