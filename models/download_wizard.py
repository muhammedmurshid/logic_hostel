from odoo import fields, models, api
import xlwt
import io
from xlsxwriter.workbook import Workbook
import base64


class DownloadHostelDetails(models.TransientModel):
    _name = 'download.hostel.details'
    _description = 'Download Hostel Details'

    hostel_id = fields.Many2many(string="Hostel", comodel_name="hostel.form", required=1)

    # def print_report(self):
    #     data = {
    #         'hostel': self.hostel_id,
    #
    #     }
    #     # docids = self.env['sale.order'].search([]).ids
    #     return self.env.ref('logic_hostel.action_hostel_pdf_download').report_action(None, data=data)
    def get_report_lines(self):
        invoice_list = []

        hostel_ids = self.hostel_id.ids

        hos = self.env['hostel.form'].search([])
        for i in hos:
            if i.id in hostel_ids:
                print(i.name, 'uu')
                if i:
                    line = {'hostel_name': i.name,
                            'hostel_rent': i.common_rent,
                            'hostel_type': i.type,
                            'hostel_contact': i.contact_number,
                            'hostel_location': i.location,
                            'hostel_gender': i.hostel_type,
                            'hostel_status': i.status
                            }
                    invoice_list.append(line)
        return invoice_list

    def print_excel_report(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/invoicing/excel_report/%s' % (self.id),
            'target': 'new',
        }
