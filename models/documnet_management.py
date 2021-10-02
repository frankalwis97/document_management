from odoo import api, fields, models
from odoo import exceptions
from odoo.exceptions import AccessError, UserError, ValidationError


class DocumentManagement(models.Model):
    _name = 'document.management'
    _description = 'Document'
    _rec_name = 'name'
    _inherit = 'mail.thread'

    name = fields.Char(string="Document Name", required="True")
    sales_order_id = fields.Many2one('sale.order', string='Sales Order')
    account_invoice_id = fields.Many2one(
        'account.invoice', string='Invoice Number')
    ir_attachment_ids = fields.Many2many(comodel_name="ir.attachment", relation="m2m_ir_attachment_relation",
                                         column1="m2m_id", column2="attachment_id", string="Attachments")

    state = fields.Selection([
        ('draft', 'Awaiting Approval'),
        ('approved', 'Approved'),
        ('rejected', "Rejected"),
    ], string='Status', readonly=True, default='draft', track_visibility="always")

    def action_change_state(self):
        """This method is incharge of changing state of the document when the 
            approve or resubmit button is clicked. Assuming that 
            only one invoice will be created the first invoice id 
            will be attached to the documents"""
        state = self.env.context.get('state_new', False)
        vals = {'state': state}

        if(len(self.account_invoice_id) == 0 and len(self.sales_order_id.invoice_ids) > 0):
            vals['account_invoice_id'] = self.sales_order_id.invoice_ids[0].id
        self.write(vals)

    def action_reject_wizard(self):
        """This method is incharge of poping the wizard to reject the document """
        return {
            'type': 'ir.actions.act_window',
            'name': 'Reject Document',
            'res_model': 'document.rejection',
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new',
        }

    def unlink(self):
        """This is to make sure approved deocuments arent deleted by anyone"""
        for document in self:
            if document.state != 'draft':
                raise UserError('You can not delete  approved  documents.')

        return super(DocumentManagement, self).unlink()
