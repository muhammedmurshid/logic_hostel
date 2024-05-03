from odoo import http
import xlsxwriter
import io
from odoo.http import request
from odoo.http import Controller, request, route, content_disposition


class InvoiceExcelReportController(http.Controller):
    @http.route([
        '/invoicing/excel_report/<model("download.hostel.details"):report_id>',
    ], type='http', auth="user", csrf=False)

    def get_sale_excel_report(self, report_id=None, **args):
        response = request.make_response(
            None,
            headers=[
                ('Content-Type', 'application/vnd.ms-excel'),
                ('Content-Disposition', content_disposition('Hostel Details' + '.xlsx'))
            ]
        )
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        header_format = workbook.add_format({
            'bold': True,
            'font_size': 12,
            'font_color': 'white',
            'bg_color': '#2C3E50',  # Background color
            'align': 'center',
            'valign': 'vcenter',
        })
        text_format = workbook.add_format({
            'bold': True,
            'font_size': 10,
            'font_color': 'black',
            'bg_color': '#ffe499',  # Background color
            'align': 'center',
            'valign': 'vcenter',
        })
        # get data for the report.
        report_lines = report_id.get_report_lines()
        # prepare excel sheet styles and formats
        sheet = workbook.add_worksheet("Hostel Details")
        sheet.write(1, 0, 'No.', header_format)
        sheet.write(1, 1, 'Hostel Name', header_format)
        sheet.write(1, 2, 'Location', header_format)
        sheet.write(1, 3, 'Contact Number', header_format)
        sheet.write(1, 4, 'Rent', header_format)
        sheet.write(1, 5, 'Type', header_format)
        sheet.write(1, 6, 'Gender', header_format)
        sheet.write(1, 7, 'Status', header_format)
        row = 2
        number = 1
        # write the report lines to the excel document
        for line in report_lines:
            print(line, 'line')
            sheet.set_row(row, 20)
            sheet.write(row, 0, number, )
            sheet.write(row, 1, line['hostel_name'], text_format)
            sheet.write(row, 2, line['hostel_location'], )
            sheet.write(row, 3, line['hostel_contact'], )
            sheet.write(row, 4, line['hostel_rent'], )
            sheet.write(row, 5, line['hostel_type'], )
            sheet.write(row, 6, line['hostel_gender'], )
            sheet.write(row, 7, line['hostel_status'], )

            row += 1
            number += 1

        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
        return response