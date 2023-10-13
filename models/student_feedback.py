from odoo import models, fields, api, _


class HostelStudentFeedback(models.Model):
    _name = 'hostel.student.feedback'
    _description = 'Hostel Student Feedback'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'student_id'

    student_id = fields.Char(string='Name', required=True)
    hostel_id = fields.Many2one('hostel.form', string='Hostel', required=True)
    feedback = fields.Text(string='Feedback')
    star_rating = fields.Selection(
        [('0', 'None'), ('1', 'Poor'), ('2', 'Fair'), ('3', 'Good'), ('4', 'Very Good'), ('5', 'Excellent')],
        readonly=True, string="Rating"
    )


class StudentsRating(models.Model):
    _name = 'students.rating'
    _description = 'Students Rating'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'student_id'

    student_id = fields.Char(string='Name', required=True)
    star_rating = fields.Selection(
        [('0', 'None'), ('1', 'Poor'), ('2', 'Fair'), ('3', 'Good'), ('4', 'Very Good'), ('5', 'Excellent')],
        readonly=True, string="Rating"
    )
    rating_id = fields.Many2one('hostel.form', string='Hostel Rating', ondelete='cascade')

    @api.depends('star_rating', 'average_rating')
    def _compute_average(self):
        for record in self:
            if record.star_rating == 0:
                print(int(record.star_rating), 'star')
                record.average_rating = 0
            else:
                print(int(record.star_rating), 'star_rating')
                average = int(record.star_rating)/5
                print(average, 'average')
                record.average_rating = average
    average_rating = fields.Float(string='Average', compute='_compute_average', store=True)
