# from odoo import http


# class Maximetest(http.Controller):
#     @http.route('/maximetest/maximetest', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/maximetest/maximetest/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('maximetest.listing', {
#             'root': '/maximetest/maximetest',
#             'objects': http.request.env['maximetest.maximetest'].search([]),
#         })

#     @http.route('/maximetest/maximetest/objects/<model("maximetest.maximetest"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('maximetest.object', {
#             'object': obj
#         })

