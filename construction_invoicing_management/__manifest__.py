
{
    'name': 'Construction Management invoices',
    'version': '1.0',
    'summary': 'Construction invoices Management Module is a specially designed module for managing and generating invoices '
               'for construction projects. This module is ideal for construction companies that need to create detailed and accurate invoices'
               ' for their clients and contractors reflecting all work completed ',
    'price': '150',
    'currency': 'USD',
    'description': """
        Construction Management
      
    """,
    'category': 'Accounting',
    'author': 'Bahyeldin Abdelhady',
    'depends': ['account', 'product', 'base_setup', 'analytic', 'portal', 'digest'],
    'data': [
        'views/account_move_views.xml',
        'security/ir.model.access.csv',
        'security/construction_security.xml',
        'views/construction_invoice.xml',
        'views/construction2_invoice.xml',
        'reports/customer_invoice_report.xml',

    ],
    'installable': True,
    'images': ['static/description/icon.png'],
    'application': True,
    'license': 'LGPL-3',
}
