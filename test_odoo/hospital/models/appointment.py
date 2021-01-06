from odoo import models, fields, api, _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('new')
        result = super(HospitalAppointment, self).create(vals)
        return result

    name = fields.Char(string='Appointment ID', required=True, copy=True, readonly=True,
                       index=True, default=lambda self: _('new'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    patient_age = fields.Integer('Age')
    notes = fields.Text(string='Registration Note')
    appointment_date = fields.Date(string='Date', required=True)
