import re
from odoo.exceptions import ValidationError,UserError
from odoo import fields, models , exceptions , api

class ContactProperty(models.Model):
    _name = 'contact.property'
    _description = 'Contact Details'

    _sql_constraints=[
        ('delivery_lead_time' , 'CHECK (lead_time >= 0)', 'Lead time cannot be negative.')
    ]

    address = fields.Text(string = 'Address')
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=True)
    contact_type = fields.Selection([
        ('farmer', 'Farmer'),
        ('buyer', 'Buyer'),
    ], required=True)
    delivery_place = fields.Selection(copy=False,
            selection=[('ahmedabad','Ahmedabad'), ('rajkot','Rajkot'), ('surat','Surat'), ('baroda','Baroda')])
    email = fields.Text(string = 'Email')
    image = fields.Image('Image', max_height=100, max_width=100, copy=False, attachment=True)
    income_certi = fields.Binary(string = 'Income Certificate by gov.') # binary fields accept all files
    language = fields.Selection(selection=[('eng','English'),('guj','Gujarati'),('hi','Hindi')])
    lead_time = fields.Integer(string="Lead time to deliver", default=4)
    name = fields.Char(string = 'Name', size=20) # The name should contain less than 20 char
    phone_number = fields.Char(string = 'Phone No.', required=True)   
    product_ids = fields.Many2many('product.property', string='Products', copy=False)
    profit = fields.Float(string='Expected Profit', compute='_compute_profit')
    purchase_offer_ids = fields.One2many('order.line','purchase_id')
    sale_offer_ids = fields.One2many('order.line','sale_id')
    purchase_order_status = fields.Selection(string='Status', default='place', copy=False,
            selection=[('place','Place Order'), ('draft','Draft')])
    sale_order_status = fields.Selection(string='Status', default='place', copy=False,
            selection=[('place','Try it!'), ('draft','Draft')])

    # phone no. constraint
    @api.constrains('phone_number')
    def _check_phone_number(self):
        for record in self:
            if record.phone_number:
                if not re.match(r'^\+?\d{10,12}$', record.phone_number):
                    raise ValidationError("Invalid phone number format. Please enter a valid phone number.")

    # eliminate duplication of buyers 
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            existing_buyer_ids = self.env['contact.property'].search([]).mapped('buyer_id') # giving the properties having some buyer ids
            l=[] # existing buyer ids
            for i in range(len(existing_buyer_ids)): #going into property and fetching ids i will be index
                #we want existing_buyer_ids[0].id
                l.append(existing_buyer_ids[i].id)
            if vals['buyer_id'] in l: #bcz it's a dict
                print('hey')
                raise UserError('This User already exist')
        return super().create(vals_list)

    # auto-set image 
    @api.onchange('buyer_id')
    def _onchange_set_image(self):
        for record in self:
            if record.buyer_id:
               record.image = record.buyer_id.image_1920

    # invoice creation
    def action_order_items(self):
        if self.purchase_offer_ids and self.purchase_order_status in ['place','draft']:
            self.purchase_order_status='place'
            for order_line in self.purchase_offer_ids:
                order_line.state = 'ordered'
        # self.write({'purchase_offer_ids':False})  # Replace field_name with the actual field name you want to clear
        # Return an action to refresh the view
        # return {'type': 'ir.actions.client', 'tag': 'reload'}

    def action_validate_items(self):
        if self.sale_offer_ids and self.sale_order_status in ['place','draft']:
            self.purchase_order_status='place'
            for order_line in self.sale_offer_ids:
                order_line.state = 'ordered'
        # self.write({'sale_offer_ids':False})  # Replace field_name with the actual field name you want to clear
        # Return an action to refresh the view
        # return {'type': 'ir.actions.client', 'tag': 'reload'}
    
    @api.onchange('purchase_offer_ids')
    def _onchange_purchase_offer_ids(self):
        if self.purchase_offer_ids and self.purchase_order_status=='place':
            self.purchase_order_status='draft'
    
    @api.onchange('sale_offer_ids')
    def _onchange_sale_offer_ids(self):
        if self.sale_offer_ids and self.sale_order_status=='place':
            self.sale_order_status='draft'

    @api.depends('product_ids.sales_price', 'sale_offer_ids.price_unit')
    def _compute_profit(self):
        for record in self:
            total_profit = 0
            for sales_line in record.sale_offer_ids: #product line
                selling_price_mentioned_product = self.env['product.property'].search([('name', '=', sales_line.name.name)]).sales_price
                total_profit += (selling_price_mentioned_product - sales_line.price_unit)*sales_line.quantity
            record.profit = total_profit
