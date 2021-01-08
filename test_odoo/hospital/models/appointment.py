from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "patient_id desc"

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
            for rec in self:
                rec.state = 'done'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
            result = super(HospitalAppointment, self).create(vals)
            return result

    def _get_default_note(self):
        return "Enter note information "

    name = fields.Char(string='Appointment ID', required=True, copy=True, readonly=True,
                       index=True, default=lambda self: _('new'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    patient_age = fields.Integer('Age', related='patient_id.patient_age')
    notes = fields.Text(string='Registration Note', default=_get_default_note)
    doctor_note = fields.Text(string='Note')
    pharmacy_note = fields.Text(string='Note')
    appointment_date = fields.Date(string='Date', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, default='draft')
