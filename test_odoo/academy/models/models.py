# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Course(models.Model):
    _name = 'academy.course'
    _description = 'Academy Course'

    name = fields.Char(string="Title", required=True, help="Name of the Course")
    description = fields.Text()

class Session(models.Model):
    _name = 'academy.session'
    _description = 'Academy Session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

