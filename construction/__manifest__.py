
{
    'name': 'Construction Invoicing Management',
    'version': '1.0',
    'summary': 'Construction Invoicing Management Module is a specially designed module for managing and generating invoices '
               'for construction projects. This module is ideal for construction companies that need to create detailed and accurate invoices'
               ' for their clients, reflecting all work completed ',
    'description': """
        <h2>Construction Invoicing Management</h2>
        <p>
            <img src="/construction/static/description/invoice.png" alt="Construction Invoicing" style="width:100%; max-width:600px;">
        </p>
        <p>
            <img src="/construction/static/description/invoice_report.png" alt="Construction Invoicing Report" style="width:100%; max-width:600px;">
        </p>
        <p>
            The <strong>Construction Invoicing Management</strong> module is a powerful tool designed for construction companies to streamline their invoicing process. This module allows you to manage all aspects of invoicing for construction projects, from tracking costs and materials to generating detailed invoices for clients.
        </p>
        Construction Invoicing Management Module is a specially designed module for managing and generating invoices '
               'for construction projects. This module is ideal for construction companies that need to create detailed and accurate invoices'
               ' for their clients, reflecting all work completed '
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
    'application': True,
    'license': 'LGPL-3',
}
