from odoo import fields, models, _, api
from odoo.exceptions import UserError


class HostelForm(models.Model):
    _name = 'hostel.form'
    _description = 'Hostel Form'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _order = 'priority desc'

    name = fields.Char(string='Name', required=True)
    contact_number = fields.Char(string='Contact number', required=True)
    location = fields.Char(string='Location')
    students_per_room = fields.Integer(string='Students per room')
    # rent = fields.Float(string='Rent', required=True)
    no_of_rooms = fields.Integer(string='No of rooms')
    status = fields.Selection(selection=[
        ('active', 'Active'), ('inactive', 'Inactive'), ('average', 'Average'),
        ('poor', 'Poor')
    ], default='active', string='status')
    common_rent = fields.Float(string='Common rent')
    rating_ids = fields.One2many(
        'students.rating', 'rating_id', string='Rating'
    )
    hostel_type = fields.Selection(
        selection=[
            ('boys', 'Boys'), ('girls', 'Girls')
        ], string='Hostel Type', required=True
    )
    facilities = fields.Html(string='Facilities')
    distance_from_institute = fields.Float(string='Distance from institute')
    branch = fields.Many2one('logic.base.branches', string='Branch')
    contact_person = fields.Char(string='Contact Person', required=True)
    caution_amount = fields.Float(string='Caution Deposit')
    caution_deposit_refundable = fields.Boolean(string='Caution Deposit Refundable')
    admission_fee = fields.Float(string='Admission Fee')
    terms_and_conditions = fields.Text(string='Terms and Conditions')
    priority = fields.Selection([('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
                                string='Priority')

    # bed share
    single_share = fields.Boolean(string='Single Share')
    single_rent = fields.Float('Rent')
    double_share = fields.Boolean(string='2 Share')
    double_rent = fields.Float('Rent')
    triple_share = fields.Boolean(string='3 Share')
    triple_rent = fields.Float('Rent')
    four_share = fields.Boolean(string='4 Share')
    four_rent = fields.Float('Rent')
    five_share = fields.Boolean(string='5 Share')
    five_rent = fields.Float('Rent')
    six_share = fields.Boolean(string='6 Share')
    six_rent = fields.Float('Rent')

    # facilities
    food_available = fields.Boolean(string='Food')
    veg_food = fields.Boolean(string='Veg Food')
    non_veg_food = fields.Boolean(string='Non Veg Food')
    both_food = fields.Boolean(string='Both Food')
    wifi = fields.Boolean(string='Wifi')
    washing_machine = fields.Boolean(string='Washing Machine')
    attached_bathroom = fields.Boolean(string='Attached Bathroom')
    time_restriction = fields.Boolean(string='Time Restriction')
    time = fields.Float(string='Time')
    study_room = fields.Boolean(string='Study Room')

    note = fields.Text(string='Note')

    @api.depends('rating_ids')
    def _average_total(self):
        for rec in self:
            total = 0
            for order in rec.rating_ids:
                print(len(order), 'len')
                if order.average_rating:
                    print('kk')
                    total += order.average_rating

                # else:
                #     print('kk')
                #     total += 0

            rec.update({
                'avg_total': total,

            })

    avg_total = fields.Float(string='Average Total', compute='_average_total')



    @api.depends('rating_ids.star_rating', 'rating_ids')
    def _compute_average(self):
        for record in self:
            if record.rating_ids:
                average = record.avg_total / len(record.rating_ids)
                record.average_rating = average
            else:
                record.average_rating = 0

    average_rating = fields.Float(
        string='Average', compute='_compute_average'
    )

    @api.depends('hostel_condition', 'average_rating')
    def _hostel_condition(self):
        for i in self:
            print(i.average_rating, 'avg')
            if i.average_rating > 0.80:
                print('excellent')
                i.hostel_condition = '5'
            if i.average_rating > 0.60 and i.average_rating <= 0.80:
                print('good')
                i.hostel_condition = '4'
            if i.average_rating > 0.4 and i.average_rating <= 0.60:
                print('fair')
                i.hostel_condition = '3'
            if i.average_rating > 0.2 and i.average_rating <= 0.40:
                print('poor')
                i.hostel_condition = '2'
            if i.average_rating > 0 and i.average_rating <= 0.20:
                print('bad')
                i.hostel_condition = '1'

            if i.average_rating == 0:
                i.hostel_condition = '0'

    hostel_condition = fields.Selection(
        selection=[
            ('0', 'None'), ('1', 'Poor'), ('2', 'Fair'), ('3', 'Good'), ('4', 'Very Good'), ('5', 'Excellent')
        ], string='Hostel Condition', compute='_hostel_condition', store=True
    )
    photo_one = fields.Binary(string='Photo One')
    photo_two = fields.Binary(string='Photo Two')
    photo_three = fields.Binary(string='Photo Three')
    currency_id = fields.Many2one(
        'res.currency', string='Currency', default=lambda self: self.env.user.company_id.currency_id
    )

    def done(self):
        print('ho')

    @api.model
    def get_hostel_datas(self):
        all_project = self.env['hostel.form'].sudo().search([])
        employees = self.env['logic.students'].sudo().search([])
        hostels = []
        for i in all_project:
            hostels.append(i.name)
        print(hostels, 'hostels')
        return {
            'total_hostel': len(all_project),
            'hostel_name': hostels,
            'total_students': len(employees),
        }
