from openerp import models, fields, api
from datetime import datetime

class wiz_age(models.TransientModel):
    _name = "wiz.age"
    _description = "Calculate student Age"

    from_date = fields.Date('From Date', required=True)
    to_date = fields.Date('To Date', required=True)

    @api.multi
    def calc_age(self):
        student_obj = self.env['student.student']
        for record in self:
            students = student_obj.search([('dob','>=',record.from_date),('dob','<=',record.to_date)])

            for student in students:
                dob = student.dob
                if dob:
                    student.age = (datetime.now() - datetime.strptime(dob,'%Y-%m-%d')).days / 365
        return True