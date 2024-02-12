from odoo import fields, models , exceptions , api
# import datetime

class ProductPricerules(models.Model):
    _name = "product.pricelist.pricerules"
    _description = "Price Rules"

    applicable = fields.Selection( #update to many2many
        string="Applicable on",
        required=True, copy=False, readonly=False, 
        selection=[('hey','Hey')],
        index='trigram',
        default='All Products',)

    min_qty = fields.Integer(
        string='Min Qty',
        default=0,
    )

    discount = fields.Float(
        string='Discount in %',
        default=5,
    )

    startdate = fields.Datetime(
        string="Start Date",
        required=True, copy=False,
    )

    end_date = fields.Datetime(
        string="End Date",
        required=True, copy=False,
    )
    