# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Andara Warehouse Customize',
    'version': '1.0',
    'category': 'Inventory',
    'sequence': 3,
    'summary': 'Custom Module for Andara Warehouse',
    'description': "No Descripsion",
    'website': 'https://bydev.tech',
    'depends': [
        'stock',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/stock_picking_form_inherit.xml',
    ],
    'demo': [],
    # 'css': ['static/src/css/crm.css'],
    'installable': True,
    'application': True,
    'auto_install': False
}