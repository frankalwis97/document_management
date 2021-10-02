from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class DocumentRejection(models.TransientModel):
    _name = 'document.rejection'
    _description = "Reject Documents"

    document_id = fields.Many2one(
        'document.management', string="Document", readonly="True")
    note = fields.Text(string="Reject Reason", required="True")

    def action_reject_document(self):
        """This method is used to log the reject reason into the mail.message model 
            so that a history of the document can be viewd"""
        state = self.env.context.get('state_new', False)
        self.document_id.message_post(
            body=("Document Rejected Due To. : %s") % (self.note), subject="Rejected")
        self.document_id.write({'state': state})

    @api.model
    def default_get(self, fields):
        res = super(DocumentRejection, self).default_get(fields)
        try:
            res["document_id"] = self.env.context.get('parent_id', False)
            
        except Exception as e: 
            print(str(e))
        return res
