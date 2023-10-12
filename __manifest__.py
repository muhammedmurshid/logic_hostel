{
    'name': "Logic Hostel",
    'version': "14.0.1.0",
    'sequence': "0",
    'depends': ['base', 'hr', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/hostel_form.xml',
        'views/student_feedback.xml',
        'views/web_feedback.xml',
    ],

    'demo': [],
    'summary': "logic_hostel_module",
    'description': "logic_hostel_module",
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
    'application': False
}
