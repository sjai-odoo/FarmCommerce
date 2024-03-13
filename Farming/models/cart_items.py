from dateutil.relativedelta import relativedelta
from odoo import models, fields, api

class CartItem(models.Model):
    _name = 'cart.item'

    state = fields.Selection(selection=[('draft','Draft'),('ordered','Ordered')], default='draft')
    product_id = fields.Many2one('product.property', string='Product', required=True)
    quantity = fields.Integer(string='Quantity', required=True)
    stop_date = fields.Datetime(compute="_compute_stop_date")
    state_id = fields.Integer(compute="_compute_state_id")

    @api.depends('create_date')
    def _compute_stop_date(self):
        for record in self:
            record.stop_date = record.create_date + relativedelta(days=3)

    @api.depends('state')
    def _compute_state_id(self):
        for record in self:
            record.state_id = 4 if (record.state=='draft') else 1
    
    @api.depends('product_id','quantity')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.product_id.name} ( {record.quantity}  kg )"