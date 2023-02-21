'''
Created on Oct 25, 2022

@author: BYDEV
'''

from odoo import fields, models, _

class MrpProduction(models.Model):
    _inherit = ['mrp.production']
    
    batch_code = fields.Char(string="Batch Code", default=1)
    
    def _get_backorder_mo_vals(self):
        
        next_seq = max(self.procurement_group_id.mrp_production_ids.mapped("backorder_sequence"), default=1)      
        # nxt_number = self.env['ir.sequence'].next_by_code('QC')       
        
        # move_lines = []
        # for move in self.browse['stock.move']:
            # if move.production_id == self.id:
                # move_lines.append(move.production_id)
        # self.env.cr.execute('''
        # select id from stock_move where production_id = %s ''',([self.id])) 
        # move_lines =  self.env.cr.fetchall()     
        
        res = super()._get_backorder_mo_vals()
        res['batch_code'] = next_seq + 1
        # self.env['qc.management.model'].create({'nolot' : nxt_number,
                                                # 'product_id' : self.product_id.id,
                                                # 'manufacture_id' : self.id,
                                                # 'batch' : self.batch_code,
                                                # # 'move_line' : (0,0, move_lines),
                                                # })        
        return res
    
    
    