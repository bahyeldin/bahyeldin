
{
    'name': 'Stock Negative Balance Preventor',
    'version': '1.0',
    'category': 'Warehouse',
    'summary': 'Prevent stock moves if there is not enough stock',
    'description': '''
        <p>This module prevents stock moves from being confirmed if there is not enough stock available.</p>
        <h3>Features</h3>
        <ul>
            <li>Checks stock availability before confirming stock moves</li>
            <li>Prevents negative stock levels</li>
            <li>Displays a warning message if stock is insufficient</li>
        </ul>
        <h3>Author</h3>
        <p>Bahyeldin Abdelhady</p>
    ''',
    'author': 'Bahyeldin Abdelhady',
    'depends': ['stock'],
    'data': [],
    'images': ['static/description/icon.png', 'static/description/thumbnail.png'],
    'installable': True,
    'auto_install': False,
}
