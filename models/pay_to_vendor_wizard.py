# my_module/wizard/pay_to_vendor_wizard.py

from odoo import api, fields, models

class paytovendorwizard(models.TransientModel):
    _name = 'pay.to.vendor.wizard'
    _description = 'Pay to Vendor Wizard'

    vendor_id = fields.Many2one('res.partner', string='Vendor', required=True)
    date = fields.Date(string='Date', required=True, default=fields.Date.context_today)
    amount = fields.Float(string='Amount', required=True)

    # @api.multi
    def action_submit(self):
        #Perform the payment logic here
        #You can create a payment record, update vendor balances, etc.
        #For example:
        self.env['account.payment'].create({
            'partner_id': self.vendor_id.id,
            'payment_date': self.date,
            'amount': self.amount,
            'payment_type': 'outbound',
            'journal_id': your_journal_id,
            # Add more fields as needed
        })
        return {'type': 'ir.actions.act_window_close'}

    # @api.multi
    # def action_cancel(self):
    #     return {'type': 'ir.actions.act_window_close'}
