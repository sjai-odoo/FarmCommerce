from odoo import fields, models , exceptions , api, Command

class ContactProperty(models.Model):
    _inherit = 'contact.property'
    
    
    def action_order_items(self):
        move_obj = self.env["account.move"]
        for record in self:
            vals = {
                'partner_id': record.buyer_id.id,
                'move_type': 'out_invoice',
                "invoice_line_ids": [
                    Command.create({
                        "name" : record.purchase_offer_ids.name.name,
                        "quantity" : record.purchase_offer_ids.quantity,
                        "price_unit" : record.purchase_offer_ids.price_unit,
                    }),
                ],
            }
            move_obj.create(vals)
        
        return super().action_order_items()
