from odoo import http
from odoo.http import request


class WebsiteForm(http.Controller):
    @http.route(['/hostel_feedback'], type='http', auth="user", website=True)
    def hostel_feedback(self):
        hostel = request.env['hostel.form'].sudo().search([])
        values = {}
        values.update({
            'hostel': hostel})

        return request.render("logic_hostel.online_hostel_feedback_form", values)

    @http.route(['/hostel_feedback/submit'], type='http', auth="user", website=True)
    def button_success(self, **post):
        print(post, 'post')
        request.env['hostel.student.feedback'].sudo().create({
            'student_id': post.get('name'),
            'hostel_id': post.get('hostel'),
            'feedback': post.get('feedback'),
            'star_rating': post.get('stars'),
        })
        hostel = request.env['hostel.form'].sudo().search([])
        for i in hostel:
            print(post.get('hostel'), 'hostel')
            print(i.id, 'id')
            rating = []
            if int(post.get('hostel')) == i.id:
                print('kk')
                res_list = {
                    'student_id': post.get('name'),
                    'star_rating': post.get('stars'),

                }
                rating.append((0, 0, res_list))
            else:
                print('na')
            i.rating_ids = rating
        return request.render("logic_hostel.tmp_online_feedback_form_thanks")


class HostelDashboard(http.Controller):
    @http.route('/dashboard', auth='user', website=True)
    def your_method(self):
        return request.render('logic_hostel.custom_dashboard_tags')

