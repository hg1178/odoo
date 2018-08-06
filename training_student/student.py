from openerp import models, fields, api
from openerp.exceptions import except_orm
from datetime import datetime


STATE = [('draft','Draft'),
         ('med_interview','Medical Intreview'),
         ('acad_interview','Academic Interview'),
         ('first_register','First Year Registered'),
         ('second_register','Second Year Registered'),
         ('third_register','Third Year Registered'),
         ('fourth_register','Fourth Year Registered'),
         ('dismiss','Dismissed'),
         ('alumni','Alumni')
]
##############################################################################################
class student_student(models.Model):
    _name = 'student.student'
    _description = 'Student Information'

    name = fields.Char(string="Name", required=True, index=True)
    active = fields.Boolean(string="Active", default=True)
    image = fields.Binary(string="Image")
    uni_no = fields.Char(string="Ministry University No", required=True, copy=False)
    seat_no = fields.Char(string="Seat No", copy=False)
    dob = fields.Date(string="Date Of Birth", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Famele'), ], default='male')
    #result_ids = fields.One2many('schoolresults_detail', 'student_id', 'School Results')
    result_ids = fields.One2many("school.results.details","student_id","School Results")
    hobbies_ids = fields.Many2many(comodel_name="hobbies.detail", relation="student_hobbies_rel", column1="student_id", column2="hobbie_id", string="Hobbies Information")
    responsible_id = fields.Many2one(comodel_name="res.partner", string="Responsible Person / Next of kin",)
    email = fields.Char(related="responsible_id.email",string="NOK Email")
    phone = fields.Char(related="responsible_id.phone", string="NOK Phone")
    fdate = fields.Date(string="First Registration Date")
    ldate = fields.Datetime(string="Last Registration Date")
    degree_id = fields.Many2one(comodel_name="degree.detail", string="Degree To Register For")
    regfees = fields.Float("Registration Fees ($)",  default=0.0)
    tutfees = fields.Float("Tuition Fees ($)",  default=0.0)
    totfees = fields.Float("Total Fees ($)", store=True, readonly=True, compute='_get_total_fees')
    ref = fields.Reference(selection=[("res.partner","partner"),("res.users","Users"),("student.student","Student")])
    ref_link = fields.Char("External Link")
    health_issues = fields.Selection([("yes","Yes",("no","No"))], "Health Issues", default="no")
    health_notes = fields.Text("Health Issue(s) Details", copy=False)
    template = fields.Html("Template")
    state = fields.Selection(STATE, "Status", readonly=True, default="draft")


##############################################################################################

class school_results_details (models.Model):
    _name = 'school.results.details'
    _description = "Student's secondary education results."

    student_id = fields.Many2one(comodel_name="student.student", string="Student", ondelete="cascade")
    subject_id = fields.Many2one(comodel_name="schoolresults.subject", string="Subject")
    results = fields.Float(string="Results")
##############################################################################################

class schoolresults_subject(models.Model):
    _name = 'schoolresults.subject'
    _description = "Student's secondary education subjects."

    name = fields.Char("Subject")
##############################################################################################

class degree_detail(models.Model):
    _name = 'degree.detail'
    _description = "A registry of all possible degrees offered by university / college."

    name = fields.Char("Name", required=True)
    # Department or faculty
    dorf_id = fields.Many2one(comodel_name="dorf.information", string="Department or Faculty", required=True)
    # Division or Department
    dord_id = fields.Many2one(comodel_name="dord.information", string="Division or Department")
    degfees = fields.Float(string="Fees per Year ($)")
##############################################################################################

class dorf_information(models.Model):
    _name = 'dorf.information'
    _rec_name = 'code'
    _description = 'A registry of all departments or faculties.'

    name = fields.Char("Name", required=True)
    code = fields.Char("Code", required=True)
    # make faculty name unique
    _sql_constraints = [
        ('dorf_code_unique',
        'UNIQUE(code)',
        "Faculty name must be unique!"),
    ]
##############################################################################################

class hobbies_detail(models.Model):
    _name = 'hobbies.detail'
    _description = 'Student Hobbies'

    name = fields.Char(string="Name", required=True)
##############################################################################################

class dord_information(models.Model):
    _name = 'dord.information'
    _rec_name = 'code'
    _description = 'A registry of all divisions or departments.'

    name = fields.Char("Name", required=True)
    code = fields.Char("Code", required=True)
    dorf_id = fields.Many2one(comodel_name="dorf.information", string="Department or Faculty", required=True)