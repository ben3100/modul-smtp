
{
    'name': 'SMTP Configuration',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Automated SMTP configuration for Odoo 16',
    'description': """
        This module automates the configuration of SMTP servers in Odoo 16.
    """,
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['base', 'mail'],
    'data': [
        'views/smtp_config_views.xml',
    ],
    'installable': True,
    'application': False,
}
