# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Andara MRP',
    'version': '1.0',
    'category': 'Manufacturing',
    'sequence': 2,
    'summary': 'Custom Module MRP Andara',
    'description': "No Descripsion",
    'website': 'https://bydev.tech',
    'depends': [
        'mrp',
        'stock',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/mrp_production_gms_inherit.xml',
    ],
    'demo': [
    ],
    # 'css': ['static/src/css/crm.css'],
    'installable': True,
    'application': True,
    'auto_install': False
}