{
    'name': "Hospital Manager",
    'summary': """Hospital Services""",
    'description': """Managing pet information""",
    'sequence': '10',
    'license': 'AGPL-3',
    'author': "HieuCa",
    'website': "odoomates.com",
    'category': 'Extra Tools',
    'version': '0.1',
    'depends': [
        'base',
        'mail',
        'sale',
    ],
    'data': [
        'data/sequence.xml',
        'data/data.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
        'wizards/create_appointment.xml',
        'views/patient_view.xml',
        'views/appointment.xml',
        'views/doctor.xml',
        'reports/patient_card.xml',
        'reports/report.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
