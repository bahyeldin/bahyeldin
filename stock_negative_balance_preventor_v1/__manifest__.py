
{
    'name': 'Stock Negative Balance Preventor V1.0',
    'version': '1.0',
    'category': 'Warehouse',
    'license': 'AGPL-3',
    'price': '10',
    'currency': 'USD',
    'summary': 'Prevent stock moves if there is not enough stock',
    'description': '''
        This module prevents stock moves from being confirmed if there is not enough stock available.
        Features
        
            Checks stock availability before confirming stock moves
            Prevents negative stock levels
            Displays a warning message if stock is insufficient
        
        
       Bahyeldin Abdelhady
    ''',
    'author': 'Bahyeldin Abdelhady',
    'depends': ['stock'],
    'data': [],
    'images': ['static/description/icon.png', 'static/description/thumbnail.jpg', 'static/description/image.jpg'],
    'installable': True,
    'auto_install': False,
}
