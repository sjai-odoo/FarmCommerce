from odoo import fields, models , exceptions , api

class ContactProperty(models.Model):
    _name = 'contact.property'
    _description = 'Contact Details'

    address = fields.Text(string = 'Address')
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    can_be_sold = fields.Boolean(string='Buyer', default=True)
    can_be_purchased = fields.Boolean(string='Farmer', default=True)
    email = fields.Text(string = 'Email')
    image = fields.Image('Image', max_height=100, max_width=100, copy=False, attachment=True)
    income_certi = fields.Binary(string = 'Income Certificate by gov.') # binary fields accept all files
    language = fields.Selection(selection=[('eng','English'),('guj','Gujarati'),('hi','Hindi')])
    name = fields.Char(string = 'Name', required=True, size=20) # The name should contain less than 20 char
    phone = fields.Integer(string = 'Phone No.', required=True)   
    product_ids = fields.Many2many('product.property', string='Products', copy=False)
    purchase_offer_ids = fields.One2many('sale.order.line','purchase_id')
    sale_offer_ids = fields.One2many('sale.order.line','sale_id')
    status = fields.Selection(string='Status', default='place', copy=False,
            selection=[('place','Place Order'), ('draft','Draft'), ('ordered','Ordered'), ('delivered','Delivered')])

    def action_order_items(self):
        if self.purchase_offer_ids and self.status in ['place','draft']:
            self.status='ordered'
    
    @api.onchange('purchase_offer_ids')
    def _onchange_purchase_offer_ids(self):
        if self.purchase_offer_ids and self.status=='place':
            self.status='draft'