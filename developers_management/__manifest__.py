{
    'name': 'Developers Management',
    'version': '16.0.1.0.0',
    'category': 'Human Resources',
    'license': 'LGPL-3',
    'application': True,
    'description': """
    Module to manage developers and their companies.
    """,

    'data': [
        'security/ir.model.access.csv',
        'views/developer_views.xml',
        'views/company_views.xml',
        'views/menu.xml',
    ],

    'test': [
        'tests/test_developer.py'
    ]
}
