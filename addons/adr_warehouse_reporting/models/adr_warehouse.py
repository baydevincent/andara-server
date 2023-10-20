'''
Created on Oct 20, 2023

@author: BYDEV
'''

from odoo import api, fields, models, _
import json

class StockPicking(models.Model):
    _inherit = ['stock.picking']
          
    def print_cst_delivery_order(self, data=None):
        data = {}
        data.update({'parameters': {
                'picking_id': self.id,
                }
        })
        
        return {
            'data': data,
            'type': 'ir.actions.report',
            'report_name': 'delivery_order',
            'report_type': 'jasper',
        }

StockPicking()
        
            

    
    
    