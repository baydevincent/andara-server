# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Andara Quality Control',
    'version': '1.0',
    'category': 'Sales',
    'sequence': 10,
    'summary': 'Sample tracking for andara',
    'description': "",
    'website': 'https://bydev.tech',
    'depends': [
        'stock','purchase', 'base', 'mrp',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/adr_qc_bp.xml',
        'views/adr_qc_bb.xml',
        'views/adr_qc_ruahan.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}