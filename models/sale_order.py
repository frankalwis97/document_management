from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    document_ids = fields.One2many(
        'document.management', 'sales_order_id', string="Documents")
    document_count = fields.Integer(
        string='Document Count', compute='_compute_document_count')


    def _compute_document_count(self):
        """Compute the amount of documents that are associated with the sales order 
        and sets it to the document_count field
        """
        for rec in self:
            Document_count = self.env['document.management'].search_count(
                [('sales_order_id', '=', rec.id)])
            rec.document_count = Document_count

    def action_open_documents(self):
        """ Assuming that only one invoice will be created the first invoice 
        id will be attached to the documents"""
        
        context = {'default_sales_order_id': self.id}
        
        if(len(self.invoice_ids) > 0):

            context.update(
                {'default_account_invoice_id': self.invoice_ids[0].id})

        action = {
            'type': 'ir.actions.act_window',
            'name': 'Documents',
            'res_model': 'document.management',
            'domain': [('sales_order_id', '=', self.id)],
            'context': context,
            'view_mode': 'tree,form',
            'target': 'current',
        }
        return action
