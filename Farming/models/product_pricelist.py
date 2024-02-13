from odoo import fields, models , exceptions , api

class ProductPricelist(models.Model):
    _name = "product.pricelist"
    _description = "Pricelists"

    pricelist_name = fields.Char(
        string="Pricelist Name",
        required=True, copy=False, readonly=False, 
        index='trigram',
        default='New Pricelist',
    )
    