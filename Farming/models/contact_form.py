from odoo import fields, models , exceptions , api
# from odoo.exceptions import UserError, RedirectWarning, ValidationError

class ContactProperty(models.Model):
    _name = "contact_property"
    _description = "Contact Details"

    name = fields.Char('Name', required=True, size=20) # The name should contain less than 20 char
    phone = fields.Integer('Phone No.', required=True)
    products_produced = fields.Selection(selection=[('wheat','Wheat'),('rice','Rice')]) # make it a related field to product categories or products
    address = fields.Text('Address')
    tags = fields.Text('Tags')
    language = fields.Selection(selection=[('eng','English'),('guj','Gujarati'),('hi','Hindi')])
    income_certi = fields.Binary('Income Certificate by gov.') # binary fields accept all files
    email = fields.Text('Email')

    # Applied constraint on phone no. to have exactly 10 digits
    
    @api.constrains('phone')
    def _check_number(self):
        number = self.phone
        if number and len(str(abs(number)))!=10: # if number is written and the length is not = 10 than raise an error
            raise ValidationError(_('Number of digits must on exceed 4'))

    # Optional code

    # _sql_constraints = [
    #     ('check_phone', 'CHECK(phone != 10)', 'Kindly recheck your phone number.'),
    # ]