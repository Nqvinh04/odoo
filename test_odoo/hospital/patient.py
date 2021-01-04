from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Record'

    patient_name = fields.Char(String='Name', required=True)
    patient_age = fields.Integer(String='Age')
    notes = fields.Text(String='Notes')
    image = fields.Binary(String='Image')
