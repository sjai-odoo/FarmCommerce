from odoo import fields, models , exceptions , api

class ProductSales(models.Model):
    _name = "product.sales"
    _description = "Product Sales Details"

    # for upselling 
    optional_pro = fields.Selection(
        string='Optional Products',#related='product.property.pro_name'
        selection=[('hey','Hey')]
        ) # doubt ask is this right way
    
    accessory_pro = fields.Selection(
        string='Accessory Products',#related='product.property.pro_name'
        selection=[('hey','Hey')],
        )
    
    # for e-commerce
    website_select = fields.Selection(
        string='Website',
        selection=[('hey','Hey')]
    ) # add afterwards

    e_categories = fields.Selection(
        string='Category',
        selection=[('hey','Hey')]
        # related='website.product.category'
    )

    product_id = fields.One2many('sale.order.line',inverse_name='product_ids')
    
