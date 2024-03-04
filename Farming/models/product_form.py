from odoo import fields, models , exceptions , api

class ProductProperty(models.Model):
    _name = 'product.property'
    _description = 'Product Details'

    color = fields.Integer(string='Color')
    cost = fields.Float('Cost per unit to sell')
    farmer_ids = fields.Many2many('contact.property')
    name = fields.Char(string='Product Name', required = True, size = 20)
    order_line_id = fields.Many2one('order.line')
    pro_category = fields.Selection(string='Category', selection=[('grains','Grains'),('vegetables','Vegetables')])
    pro_image = fields.Image(string='Image', max_height = 500, max_width = 500)
    quantity = fields.Float('Quantity (in kg)')
    sales_price = fields.Float('W/O tax', compute='_compute_cost')  
    tax = fields.Selection(string='Tax', selection=[( '5','5% tax'),( '15', 'Base 15%'),( '21', '21% tax')])

    @api.depends('tax', 'cost')
    def _compute_cost(self):
        for record in self:
            record.sales_price = record.cost*(1 - int(record.tax)/100)
    
    # @api.onchange('farmer_ids.sale_offer_ids')
    # def _onchange_quantity(self):
    #     for record in self:
    #         breakpoint()
    #         required_contacts = self.env['contact.property'].filtered(lambda property : property.contact_type == 'farmer' )
    #         required_order_lines = required_contacts.sale_offer_ids.filtered( lambda x: x.name == record.name)
    #         record.quantity = sum(required_order_lines.mapped('quantity'))
