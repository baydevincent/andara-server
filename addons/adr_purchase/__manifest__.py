# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Andara Purchase',
    'version': '1.0',
    'category': 'Purchasing',
    'sequence': 3,
    'summary': 'Custom Module for Andara Purchase',
    'description': "No Descripsion",
    'website': 'https://bydev.tech',
    'depends': [
        'purchase',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/adr_purchase_form_inherit.xml',
        'views/res_partner_rekening.xml',
    ],
    'demo': [],
    # 'css': ['static/src/css/crm.css'],
    'installable': True,
    'application': True,
    'auto_install': False
}