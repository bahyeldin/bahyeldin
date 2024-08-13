
{
    'name': 'Construction Invoicing Management',
    'version': '1.0',
    'summary': 'Construction Invoicing Management Module is a specially designed module for managing and generating invoices '
               'for construction projects. This module is ideal for construction companies that need to create detailed and accurate invoices'
               ' for their clients, reflecting all work completed ',
    'price': '15',
    'currency': 'USD',
    'description': """
        Construction Invoicing Management
      
    """,
    'category': 'Accounting',
    'author': 'Bahyeldin Abdelhady',
    'depends': ['account', 'product', 'base_setup', 'analytic', 'portal', 'digest'],
    'data': [
        'views/account_move_views.xml',
        'views/construction_invoice.xml',
        'reports/customer_invoice_report.xml',

    ],
    'installable': True,
    'images': ['static/description/invoice_report.png'],
    'application': True,
    'license': 'LGPL-3',
}
