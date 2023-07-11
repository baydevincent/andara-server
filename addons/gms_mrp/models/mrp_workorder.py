'''
Created on Oct 25, 2022

@author: BYDEV
'''

from odoo import fields, models, _

class MrpWorkcenterProductivity(models.Model):
    _inherit = ['mrp.workorder']
    
    operator_name = fields.Char(string="Operator")