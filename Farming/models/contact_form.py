from odoo import fields, models , exceptions , api
# from odoo.exceptions import UserError, RedirectWarning, ValidationError

class ContactProperty(models.Model):
    _name = 'contact.property'
    _description = 'Contact Details'

    name = fields.Char(string = 'Name', required=True, size=20) # The name should contain less than 20 char
    phone = fields.Integer(string = 'Phone No.', required=True)   
    can_be_sold = fields.Boolean(string='Can be Sold', default=True)
    can_be_purchased = fields.Boolean(string='Can be Purchased', default=True)
    address = fields.Text(string = 'Address')
    language = fields.Selection(selection=[('eng','English'),('guj','Gujarati'),('hi','Hindi')])
    income_certi = fields.Binary(string = 'Income Certificate by gov.') # binary fields accept all files
    email = fields.Text(string = 'Email')
    category = fields.Many2many('product.property', string='Categories')

    # Applied constraint on phone no. to have exactly 10 digits
    
    @api.constrains('phone')
    def _check_number(self):
        number = self.phone
        if number and len(str(abs(number)))!=10: # if number is written and the length is not = 10 than raise an error
            raise ValidationError(_('Number of digits must on exceed 10'))

    