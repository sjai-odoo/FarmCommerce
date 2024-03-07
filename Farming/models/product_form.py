from odoo import fields, models , exceptions , api

class ProductProperty(models.Model):
    _name = 'product.property'
    _description = 'Product Details'

    color = fields.Integer(string='Color')
    cost = fields.Float('Cost per unit to sell', compute='_compute_cost')
    farmer_ids = fields.Many2many('contact.property')
    image = fields.Binary() # for website
    name = fields.Char(string='Product Name', required = True, size = 20)
    order_line_id = fields.Many2one('order.line') # just to show products on order lines
    pro_category = fields.Selection(string='Category', selection=[('grains','Grains'),('vegetables','Vegetables')])
    quantity = fields.Float('Quantity (in kg)', compute="_compute_quantity", default=0)
    sales_price = fields.Float('W/O tax')  
    tax = fields.Selection(string='Tax', selection=[( '5','5% tax'),( '15', 'Base 15%'),( '21', '21% tax')])

    @api.depends('tax', 'sales_price')
    def _compute_cost(self):
        for record in self:
            record.cost = record.sales_price*(1 + int(record.tax)/100)
    
    @api.depends('order_line_id')
    def _compute_quantity(self):
        for record in self:
            quantity=record.quantity
            # same product na records
            req_records = self.env['order.line'].search([('name', '=', record.name)])
            for record_wise in req_records: # filter those which are uploaded by farmers
                if(record_wise.sale_id):
                    quantity += record_wise.quantity
                else:
                    pass
            record.quantity=quantity


    # @api.onchange('farmer_ids.sale_offer_ids')
    # def _onchange_quantity(self):
    #     for record in self:
    #         breakpoint()
    #         required_contacts = self.env['contact.property'].filtered(lambda property : property.contact_type == 'farmer' )
    #         required_order_lines = required_contacts.sale_offer_ids.filtered( lambda x: x.name == record.name)
    #         record.quantity = sum(required_order_lines.mapped('quantity'))
