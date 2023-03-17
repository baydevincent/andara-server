'''
Created on Mar 17, 2023

@author: BYDEV
'''

from odoo import api, fields, models, _
# from odoo.exceptions import UserError,Warning


class ADRQualityControl(models.Model):
    _name = "adr.qc"
    _description = "Andara Monthly Budgeting"
                
    name = fields.Char(string='Document Code', required=True, copy=False, index=True, default=lambda self: _('New'))
    code = fields.Char(string='Kode', default=lambda self: _('-'))
    no_bets = fields.Char(sting='Nomor Bets', default=lambda self: _('-'))
    expr_date = fields.Date(string='Tanggal Kadaluarsa', default=fields.Datetime.now)
    sample_pick_date = fields.Date(string='Tanggal pengambilan Sampel')
    responsible_id = fields.Many2one('res.users', string='Responsible', states={'done': [('readonly', True)], 'confirmed': [('readonly', True)]})
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    incoming_prod = fields.Float(string='Barang Datang')
    sample_qty  = fields.Float(string='Sample yang di ambil')
    reject_qty = fields.Float(string='Sampel yang Reject')
    score_value = fields.Selection(string='Hasil Pemeriksaan', selection=[('lulus', 'DILULUSKAN'),
                                                                          ('reject', 'DITOLAK')])
    color = fields.Selection(string='Warna', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    text_label = fields.Selection(string='Tulisan', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    composition_type = fields.Selection(string='Jenis Bahan', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    spray_test = fields.Selection(string='Spray', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    tutup = fields.Selection(string='Tutup', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    dimension = fields.Selection(string='Ukuran Dimensi', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    drain_test = fields.Selection(string='Uji Kebocoran', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    product_desc = fields.Many2one('product.template', string='Product')
    
    
    @api.model
    def create(self,vals):
        vals = vals
        name = self.env['ir.sequence'].next_by_code('self.qc.docs')
        if vals['name'] == 'New':      
            vals.update({'name' : name})
        result = super(ADRQualityControl, self).create(vals)
        return result
    

               

        

        

    