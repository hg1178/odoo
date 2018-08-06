# -*- coding: utf-8 -*-

from openerp import models, fields, api


class student_student(models.Model):
    _name = 'student.student'

    # @api.depends('dob')
    # def calculate_age(self):
    #     """ Description:- This method calculates the age on the basis of the
    #     Birth Date entered in the 'dob' field. """
    #     for data in self:
    #         if data.dob:
    #             current_year = datetime.datetime.now().year
    #             birth_year = datetime.datetime.strptime(data.dob, "%Y-%m-%d").year
    #             age = current_year - birth_year
    #             data.age = age

    # Basic Fields
    name = fields.Char('Student Name')
    email = fields.Char('Email')
    contact = fields.Char('Contact Number')
    dob = fields.Date('Date of Birth')
    registration_date = fields.Datetime('Registration Date')
    is_physically_disabled = fields.Boolean('Is Physically Disabled?')
    image = fields.Binary('Image')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    # Relational Fields
    course_id = fields.Many2one('course.course', string='Course')
    hobby_ids = fields.Many2many('hobby.hobby', 'student_hobbies_rel', 'student_id', 'hobby_id', string='Hobby')
    qualification_ids = fields.One2many('qualification.qualification', 'student_id', string='Qualification')
    # Computed Field
    age = fields.Float(string='Age')


class qualification_qualification(models.Model):
    _name = 'qualification.qualification'

    student_id = fields.Many2one('student.student', string='Student')
    course_id = fields.Many2one('course.course', string='Course')
    year_cleared = fields.Date('Completed On')
    grade = fields.Float('Grade(%)')


class course_course(models.Model):
    _name = 'course.course'

    name = fields.Char('Course Name')


class hobby_hobby(models.Model):
    _name = 'hobby.hobby'

    name = fields.Char('Hobby Name')