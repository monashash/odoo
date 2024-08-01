{
    'name': 'Sale Order',
    'version': '1.0',
    'summary': 'Custom approval levels for sale orders',
    
    'author': 'mona khaled',
    'category': 'Sales Management',
    'depends': ['sale'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
