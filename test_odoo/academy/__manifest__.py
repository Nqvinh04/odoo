# -*- coding: utf-8 -*-
{
    'name': "academy",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "Hieu Ca",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/academy.xml',
        # 'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installation': True,
    'application': True,
    'auto_install': False,
}
