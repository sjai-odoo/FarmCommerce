from odoo import fields, models , exceptions , api
import datetime

class sales(models.Model):
    _name = "sales.order"
    _description = "Sales Order"

    # fields
    partner = fields.Many2one('res.partner', string="Customer", required=True) 
    state = fields.Selection(selection=[('draft', "Quotation"),('sent', "Quotation Sent"),('sale', "Sales Order"),('cancel', "Cancelled"),], string="Status", copy=False, index=True, default='draft')
    date_order = fields.Date(string="Order Date", required=True, copy=False, default=fields.Datetime.now )
    create_date = fields.Date(string="Creation Date", index=True) 
    invoice_status = fields.Selection(selection=[('invoiced', 'Fully Invoiced'),('to invoice', 'To Invoice'),], string="Invoice Status", store=True)
    offers = fields.One2many('sale.order.line','sales_id')
