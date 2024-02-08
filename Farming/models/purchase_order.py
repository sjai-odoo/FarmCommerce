from odoo import fields, models , exceptions , api
from datetime import timedelta

SALE_ORDER_STATE = [
    ('rfq', "RFQ"),
    ('confirmed', "Confirmed"),
    ('po', "Purchase Order"),
]

TAXES = [
    ( 5,'5% tax'),
    ( 15, 'Base 15%'),
    ( 21, '21% tax'),
]

class Purchase(models.Model):
    _name = "Purchase.order"
    _description = "Purchase Order"
    _order = 'date_order desc, id desc'
    _sql_constraints = [
        ('date_order_conditional_required',
         "CHECK((state = 'sale' AND date_order IS NOT NULL) OR state != 'sale')",
         "A confirmed sales order requires a confirmation date."),
    ]

    # fields

    name = fields.Char(
        string="Buyer",
        required=True, copy=False, readonly=False, 
        index='trigram',
        default='New',
        related='contact.property.name') 

    state = fields.Selection(
        selection=SALE_ORDER_STATE,
        string="Status",
        readonly=True, copy=False, index=True,
        default='draft')

    deadline = fields.Datetime(  # Billing Date
        string="Order Deadline", index=True, readonly=True)

    arrival = fields.Datetime( # Ordered date
        string="Expected Arrival",
        required=True, copy=False,
        default=datetime.datetime.now().day + '/' + datetime.datetime.now().month + '/' + datetime.datetime.now().year
    )

    