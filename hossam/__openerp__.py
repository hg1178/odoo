{
    'name': 'Student Registration Managment',
    'description': 'A student registration managment module',
    'category': 'Student',
    'author': 'Hossam Galal',
    'website': 'https://www.facebook.com/hossam.galal.982',
    'depends': ['base', 'sale'],
    'sequence': '3',
    'data': ['security/security_view.xml',
             'view/student_view.xml',
             'view/degree_view.xml',
             'wizard/wiz_calc_age_view.xml',
             'report/student_report.xml',
             'report/student_profile.xml'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
