# -*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class EventEvent(models.Model):
    _inherit = 'event.event'

    employee_ids = fields.Many2many('hr.employee', string='Employees')

    @api.onchange('employee_ids', 'date_begin', 'date_end')
    def _onchange_employee_ids(self):

        warning = {}
        domain = [
            # ('id', '!=', event.id),
            ('employee_ids', 'in', self.employee_ids.ids),
            '|', '|',
            '&', ('date_begin', '<=', self.date_begin), ('date_end', '>=', self.date_begin),
            '&', ('date_begin', '<=', self.date_end), ('date_end', '>=', self.date_end),
            '&', ('date_begin', '<=', self.date_begin), ('date_end', '>=', self.date_end),
        ]

        if self.search_count(domain) > 0:
            warning = {
                    'title': 'Error',
                    'message': 'This Employee is already busy for this time.',
            }
        if warning:
            return {'warning': warning}

    @api.onchange('address_id', 'date_begin', 'date_end')
    def _onchange_address_id(self):

        warning = {}
        domain = [
            ('address_id', '=', self.address_id.id),
            '|', '|',
            '&', ('date_begin', '<=', self.date_begin), ('date_end', '>=', self.date_begin),
            '&', ('date_begin', '<=', self.date_end), ('date_end', '>=', self.date_end),
            '&', ('date_begin', '<=', self.date_begin), ('date_end', '>=', self.date_end),
        ]

        if self.search_count(domain) > 0:
            warning = {
                    'title': 'Error',
                    'message': 'This Location is already busy for this time.',
            }
        if warning:
            return {'warning': warning}

    @api.onchange('organizer_id', 'date_begin', 'date_end')
    def _onchange_organizer_id(self):

        warning = {}
        domain = [
            ('organizer_id', '=', self.organizer_id.id),
            '|', '|',
            '&', ('date_begin', '<=', self.date_begin), ('date_end', '>=', self.date_begin),
            '&', ('date_begin', '<=', self.date_end), ('date_end', '>=', self.date_end),
            '&', ('date_begin', '<=', self.date_begin), ('date_end', '>=', self.date_end),
        ]

        if self.search_count(domain) > 0:
            warning = {
                    'title': 'Error',
                    'message': 'This Organizer is already busy for this time.',
            }
        if warning:
            return {'warning': warning}
