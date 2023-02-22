'''
Created on Oct 25, 2022

@author: BYDEV
'''

from odoo import api, fields, models, _

class PurchaseOrder(models.Model):
    _inherit = ['purchase.order']
    
    rekening = fields.Char(string="No Rekening")
    
    @api.onchange('partner_id')
    def get_rekening(self):
        
        for this in self:        
            value = this.partner_id.no_rek
            
            self.write({'rekening' : value}),
         
PurchaseOrder()

class ResPartner(models.Model):
    _inherit = ['res.partner']
    
    no_rek = fields.Char(string="No Rekening")
        
            

    
    
    