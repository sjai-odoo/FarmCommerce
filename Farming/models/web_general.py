from odoo import fields, models , exceptions , api

class Website(models.Model):
    _name = "website.product"
    _description = "Product Sales"
    _inherit = 'product.property'

    # all other will be inherited from product 
    category = fields.Selection(
        string='Category on web',
        selection=[('grains',"Grains"),('vegetables','Vegetables')])
    