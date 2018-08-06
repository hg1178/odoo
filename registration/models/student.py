# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class registration(models.Model):
#     _name = 'registration.registration'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100



STATE = [{'draft','Draft'},
         {'med_interview','Medical Intreview'},
         {'acad_interview','Academic Interview'},
         {'first_register','First Year Registered'},
         {'second_register','Second Year Registered'},
         {'third_register','Third Year Registered'},
         {'fourth_register','Fourth Year Registered'},
         {'dismiss','Dismissed'},
         {'alumni','Alumni'}
]

#################################################################################


class student_student(models.Model):
    _name = 'student.student'
    _description = 'Student Information'

    name = fields.Char(string="Name",required=True,index=True)
    active = fields.Boolean(string="Active",default=True)
    image = fields.Binary(string="Image")
    uni_no = fields.Char(string="Ministry University No",required=True,copy=False)
    seat_no = fields.Char(string="Seat No", copy=False)
    dob = fields.Date(string="Date of Birth", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female')], default="male")
    result_ids = fields.One2many(comodel_name="", inverse_name="", string="", required=False, )



#################################################################################

class school_results_detail(models.Model):
    _name = 'school.results.detail'
    _description = "Student's secondary education results"

    student_id = fields.Many2one(comodel_name="student.stedunt", string="Student", ondelete="cascade")
    subject_id = fields.Many2one(comodel_name="", string="Subject")
    results = fields.Float(string="Results")

#################################################################################

class school_results_subject(models.Model):
    _name = 'school.results.subject'
    _description = "Student's secondary education subjects"

    name = fields.Char("Subject")

#################################################################################