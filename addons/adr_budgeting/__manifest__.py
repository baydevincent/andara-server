# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Andara Monthly Budgeting',
    'version': '1.0',
    'category': 'Accounting',
    'sequence': 10,
    'summary': 'Manage Monthly Budgeting for andara',
    'description': "",
    'website': 'https://bydev.tech',
    'depends': [
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/adr_budget_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}