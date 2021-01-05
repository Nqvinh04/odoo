from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class MyPet(models.Model):
    _name = "my.pet"
    _description = "My pet model"

    name = fields.Char('Pet Name', required=True)
    nickname = fields.Char('Nickname')
    description = fields.Text('Pet Description')
    age = fields.Integer('Pet Age', default=1)
    weight = fields.Float('Weight (kg)')
    dob = fields.Date('DOB', required=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', default='male')
    pet_image = fields.Binary("Pet Image", attachment=True, help="Pet Image")
    owner_id = fields.Many2one('res.partner', string='Owner')
    product_ids = fields.Many2many(comodel_name='product.product',
                                   string="Related Products",
                                     relation='pet_product_rel',
                                   column1='col_pet_id',
                                   column2='col_product_id')
    basic_price = fields.Float('Basic Price', default=0)

# Char: text 1 dòng
# Text: textarea nhiều dòng
# Integer: số nguyên
# Float: số thực
# Date: ngày tháng năm
# Selection: chọn lựa, option
# Binary: lưu ảnh
# Many2one: quan hệ nhiều một: N-1
# Many2many: quan hệ nhiều nhiều: N-N
