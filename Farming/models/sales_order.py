from odoo import fields, models , exceptions , api
import datetime

SALE_ORDER_STATE = [
    ('draft', "Quotation"),
    ('sent', "Quotation Sent"),
    ('sale', "Sales Order"),
    ('cancel', "Cancelled"),
]

INVOICE_STATUS = [
    ('invoiced', 'Fully Invoiced'),
    ('to invoice', 'To Invoice'),
]

TAXES = [
    ( '5','5% tax'),
    ( '15', 'Base 15%'),
    ( '21', '21% tax'),
]

class sales(models.Model):
    _name = "sales.order"
    _description = "Sales Order"
    _order = 'date_order desc, id desc'

    # fields

    name = fields.Char(
        string="Customer",
        required=True, copy=False, readonly=False, 
        index='trigram',
        default='New',
        # related='contact.property.name'
        ) 

    state = fields.Selection(
        selection=SALE_ORDER_STATE,
        string="Status",
        readonly=True, copy=False, index=True,
        default='draft')

    create_date = fields.Datetime(  # Billing Date
        string="Creation Date", index=True, readonly=True)

    date_order = fields.Datetime( # Ordered date
        string="Order Date",
        required=True, copy=False,
        default=datetime.datetime.now().day         )

    # billing amount related fields
    
    # amount_tax = fields.Monetary(string="Tax", store=True) # total taxable amount
    # amount_total = fields.Monetary(string="Total", store=True) # total amount
    # amount_invoiced = fields.Monetary(string="Already invoiced", compute='_compute_amount_invoiced')

    invoice_status = fields.Selection(
        selection=INVOICE_STATUS,
        string="Invoice Status",
        compute='_compute_invoice_status',
        store=True)
