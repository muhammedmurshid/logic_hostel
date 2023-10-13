from odoo import models, fields, api, _


class PosDashboard(models.Model):
    _inherit = 'project.project'

    @api.model
    def get_tiles_data(self):
        all_project = self.env['project.project'].search([])
        all_task = self.env['project.task'].search([])
        analytic_project = self.env['account.analytic.line'].search([])
        total_time = sum(analytic_project.mapped('unit_amount'))
        employees = self.env['hr.employee'].search([])
        task = self.env['project.task'].search_read([
            ('sale_order_id', '!=', False)
        ], ['sale_order_id'])
        task_so_ids = [o['sale_order_id'][0] for o in task]
        sale_orders = self.mapped('sale_line_id.order_id') | self.env['sale.order'].browse(task_so_ids)
        return {
            'total_projects': len(all_project),
            'total_tasks': len(all_task),
            'total_employees': len(employees),
        }
