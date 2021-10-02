import logging
from odoo import api, fields, models
from odoo.exceptions import UserError

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    document_ids = fields.One2many('document.management', 'account_invoice_id', string="Documents")
    document_count = fields.Integer(string='Document Count', compute='_compute_document_count')

    
    def _compute_document_count(self):
        """Compute the amount of approved documents that are associated with the invoice"""
        for rec in self:
            Document_count = self.env['document.management'].search_count(
                [('account_invoice_id', '=', rec.id), ('state', '=', 'approved')])
            rec.document_count = Document_count

    def action_open_documents(self):
        """The default_sales_order_id wont be passed so that user cannot 
           save any documents created in the invoice since sales order id is mandatory."""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Documents',
            'res_model': 'document.management',
            'domain': [('account_invoice_id', '=', self.id), ('state', '=', 'approved')],
            'context': {'default_account_invoice_id': self.id},
            'view_mode': 'tree,form',
            'target': 'current',
        }

    @api.model
    def create(self, vals):
        """Here when the invoice is created all the documents that are approved 
        will be updated with the current invoice ID if the invoice id is null in the documents."""
        result = super(AccountInvoice, self).create(vals)
        try:
            Sales = self.env['sale.order'].search([('name', '=', result.origin)])
            documents = Sales.document_ids
            if(len(documents) > 0):
                for document in documents:
                    if(document.state == 'approved' and len(document.account_invoice_id) == 0):
                        document.write({'account_invoice_id': result.id})
        except Exception as e: 
            print(str(e))

        return result
