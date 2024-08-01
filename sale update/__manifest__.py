{
    'name': 'Sales Update',
    'version': '1.0',
    'summary': 'A custom module to update sales features',
    'description': 'This module provides custom updates and features for sales management.',
    'author': 'mona khaled',
    'category': 'Sales',
    'depends': ['sale'],
    'data': [
        'views/sale_order_views.xml',
        'views/sale_update_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
      'auto_install': False,
}
