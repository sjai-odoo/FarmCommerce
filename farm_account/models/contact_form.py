from datetime import datetime
from odoo import fields, models , exceptions , api, Command

class ContactProperty(models.Model):
    _inherit = 'contact.property'
    

    def action_order_items(self):
        move_obj = self.env["account.move"]
        for record in self:
            invoice_lines = []
            for purchase_order in record.purchase_offer_ids.search([('state', '!=', 'ordered')]):
                invoice_line = (0, 0, {
                    "name": purchase_order.name.name,
                    "quantity": purchase_order.quantity,
                    "price_unit": purchase_order.buyer_price_unit,
                })
                invoice_lines.append(invoice_line)
            vals = {
                'partner_id': record.buyer_id.id,
                'move_type': 'out_invoice',
                "invoice_line_ids": invoice_lines,
            }
            move_obj.create(vals)
        return super().action_order_items()

        # for record in self:
        #     record.purchase_offer_ids.unlink()
    
    def action_validate_items(self):
        move_obj = self.env["account.move"]
        for record in self:
            # Prepare the list of invoice lines
            vendor_invoice_lines = []
            for sale_order in record.sale_offer_ids.search([('state', '!=', 'ordered')]):
                invoice_line = (0, 0, {
                    "name": sale_order.name.name,
                    "quantity": sale_order.quantity,
                    "price_unit": sale_order.price_unit,
                })
                vendor_invoice_lines.append(invoice_line)

            # Create the bill
            vals = {
                'partner_id': 1,  # Assuming partner_id represents the vendor
                'move_type': 'in_invoice',  # This is for vendor bills
                'invoice_date': datetime.now().date(),
                'invoice_line_ids': vendor_invoice_lines,
            }
            bill = move_obj.create(vals)
            

        # Call super() only once after processing all records
        return super().action_validate_items()

        # def action_show_history(self):
        #     move_obj = self.env['account.move']
        #     breakpoint()
        
        