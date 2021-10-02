# -*- coding: utf-8 -*-
from odoo import http

# class DocumentManagement(http.Controller):
#     @http.route('/document_management/document_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/document_management/document_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('document_management.listing', {
#             'root': '/document_management/document_management',
#             'objects': http.request.env['document_management.document_management'].search([]),
#         })

#     @http.route('/document_management/document_management/objects/<model("document_management.document_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('document_management.object', {
#             'object': obj
#         })