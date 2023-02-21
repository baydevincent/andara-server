'''
Created on Oct 25, 2022

@author: BYDEV
'''

from odoo import api, fields, models, _


class QCManagement(models.Model):
    _name = "qc.management.model"
    _description = "Quality Control"

    @api.depends('manufacture_id')
    def _get_lines(self):
        line_obj = self.env['stock.move'].browse()
        move_line = []
        
        for move in line_obj:
            if self.manufacture_id in move.production_id:
                move_line.append(move.id)
                self.env.write({'move_line' : [move_line]
                            })
                
    nolot = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, states={'draft': [('readonly', False)]}, index=True, default=lambda self: _('New'))
    product_id = fields.Many2one('product.product', string='Product', required=False)
    batch = fields.Char(string='Kode Batch ', required=False, readonly=True)
    manufacture_id = fields.Many2one('mrp.production', string='Manufacturing Order', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Quotation Sent'),
        ('in_progress', 'Sales Order'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    customer_id = fields.Many2one('res.partner', string='Customer', required=False)
    date_order = fields.Datetime(string='Tanggal Order', 
                                 required=True, readonly=True, index=True, 
                                 states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, 
                                 copy=False, default=fields.Datetime.now)   
    move_line = fields.One2many('stock.move','production_id', string='Product Line',
                                 compute=_get_lines, store=True)
    
        
        

    