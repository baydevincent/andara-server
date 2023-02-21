# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Andara QC Management',
    'version': '1.0',
    'category': 'Manufacture',
    'sequence': 15,
    'summary': 'Manage quality of production and lot splitting',
    'description': "",
    'website': 'https://bydev.tech',
    'depends': [
        'mrp',
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/sale_custom_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}