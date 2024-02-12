from odoo import fields, models , exceptions , api

CONTROL_POLICY = [
    ( 'on_ordered','On Ordered quantities'),
    ( 'on_delivered','On Delivered quantities'),
]

class ProductPurchase(models.Model):
    _name = "product.purchase"
    _description = "Product Purchase Details"

    vendor = fields.Selection(
        string='Vendor',
        # related='contact.property.name'
        selection=[('name','Name')]
    )

    price = fields.Float(
        string='Price',
        # doubt how to match with the product name's price of that vendor
    )

    vendor_tax = fields.Integer(
        string='Vendor tax',
        # related='product.property.tax'
    )

    control_policy = fields.Selection(
        string='Control Policy',
        selection=CONTROL_POLICY,
    )