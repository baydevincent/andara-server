'''
Created on Oct 25, 2022

@author: BYDEV
'''

from odoo import api, fields, models, _

class StockPicking(models.Model):
    _inherit = ['stock.picking']
    supp_doc = fields.Char(string="No SJ Supplier", required=True)
            
StockPicking()

        
            

    
    
    