'''
Created on Mar 17, 2023

@author: BYDEV
'''

from odoo import api, fields, models, _
# from odoo.exceptions import UserError,Warning


class ADRBahanKemas(models.Model):
    _name = "adr.qc.kemas"
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
        name = self.env['ir.sequence'].next_by_code('self.qc.docs.kms')
        if vals['name'] == 'New':      
            vals.update({'name' : name})
        result = super(ADRBahanKemas, self).create(vals)
        return result
    
class ADRProdukRuah(models.Model):
    _name = "adr.qc.ruah"
    _description = "Andara Monthly Budgeting"
                
    name = fields.Char(string='Document Code', required=True, copy=False, index=True, default=lambda self: _('New'))
    product_code = fields.Char(string='Kode Product', default=lambda self: _('-'))
    no_bets = fields.Char(sting='Nomor Bets', default=lambda self: _('-'))
    production_date = fields.Date(string='Tanggal Produksi')
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
    bentuk = fields.Selection(string='Bentuk (Standar Cair)', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    warna = fields.Selection(string='Warna (Standar Bening)', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    bau = fields.Selection(string='Bau (Standar Khas)', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    kejernihan = fields.Selection(string='Kejernihan (Standar Jernih)', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    homogeni = fields.Selection(string='Homogenitas (Standar Homogen)', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    product_desc = fields.Many2one('product.template', string='Product')   
    note = fields.Text('Keterangan')
    
    @api.model
    def create(self,vals):
        vals = vals
        name = self.env['ir.sequence'].next_by_code('self.qc.docs.rh')
        if vals['name'] == 'New':      
            vals.update({'name' : name})
        result = super(ADRProdukRuah, self).create(vals)
        return result
    
class ADRBahanBaku(models.Model):
    _name = "adr.qc.bb"
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
    cert_analisis = fields.Selection(string='Sertifikat Analisis', selection=[('pass', 'Sesuai'),
                                                                             ('reject', 'Tidak Sesuai')])
    cert_analisis_sample = fields.Selection(string='Sample', selection=[('1', '1'),
                                                                        ('2', '2'),
                                                                        ('3', '3'),
                                                                        ('4', '4'),
                                                                        ('5', '5'),
                                                                        ('6', '6'),
                                                                        ('7', '7'),
                                                                        ('8', '8'),
                                                                        ('9', '9'),
                                                                        ('10', '10'),])
    msds = fields.Selection(string='MSDS', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    msds_sample = fields.Selection(string='Sample', selection=[('1', '1'),
                                                               ('2', '2'),
                                                               ('3', '3'),
                                                               ('4', '4'),
                                                               ('5', '5'),
                                                               ('6', '6'),
                                                               ('7', '7'),
                                                               ('8', '8'),
                                                               ('9', '9'),
                                                               ('10', '10'),])
    ifra = fields.Selection(string='IFRA', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    ifra_sample = fields.Selection(string='Sample', selection=[('1', '1'),
                                                               ('2', '2'),
                                                               ('3', '3'),
                                                               ('4', '4'),
                                                               ('5', '5'),
                                                               ('6', '6'),
                                                               ('7', '7'),
                                                               ('8', '8'),
                                                               ('9', '9'),
                                                               ('10', '10'),])
    label = fields.Selection(string='Label', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    label_sample = fields.Selection(string='Sample', selection=[('1', '1'),
                                                                ('2', '2'),
                                                                ('3', '3'),
                                                                ('4', '4'),
                                                                ('5', '5'),
                                                                ('6', '6'),
                                                                ('7', '7'),
                                                                ('8', '8'),
                                                                ('9', '9'),
                                                                ('10', '10'),])
    kemasan = fields.Selection(string='Kemasan', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    kemasan_sample = fields.Selection(string='Sample', selection=[('1', '1'),
                                                                        ('2', '2'),
                                                                        ('3', '3'),
                                                                        ('4', '4'),
                                                                        ('5', '5'),
                                                                        ('6', '6'),
                                                                        ('7', '7'),
                                                                        ('8', '8'),
                                                                        ('9', '9'),
                                                                        ('10', '10'),])
    warna = fields.Selection(string='Warna', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    warna_sample = fields.Selection(string='Sample', selection=[('1', '1'),
                                                                ('2', '2'),
                                                                ('3', '3'),
                                                                ('4', '4'),
                                                                ('5', '5'),
                                                                ('6', '6'),
                                                                ('7', '7'),
                                                                ('8', '8'),
                                                                ('9', '9'),
                                                                ('10', '10'),])
    aroma = fields.Selection(string='Aroma', selection=[('pass', 'Sesuai'),
                                                        ('reject', 'Tidak Sesuai')])
    aroma_sample = fields.Selection(string='Sample', selection=[('1', '1'),
                                                                ('2', '2'),
                                                                ('3', '3'),
                                                                ('4', '4'),
                                                                ('5', '5'),
                                                                ('6', '6'),
                                                                ('7', '7'),
                                                                ('8', '8'),
                                                                ('9', '9'),
                                                                ('10', '10'),])
    product_desc = fields.Many2one('product.template', string='Product')
    note = fields.Text(string='Note')

    
    
    @api.model
    def create(self,vals):
        vals = vals
        name = self.env['ir.sequence'].next_by_code('self.qc.docs.bb')
        if vals['name'] == 'New':      
            vals.update({'name' : name})
        result = super(ADRBahanBaku, self).create(vals)
        return result
    
class ADRBahanJadi(models.Model):
    _name = "adr.qc.bj"
    _description = "Andara QC BJ"
                
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
    warna = fields.Selection(string='Warna Dasar', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    warna_text = fields.Selection(string='Warna Tulisan', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    logo = fields.Selection(string='Logo', selection=[('pass', 'Sesuai'),
                                                      ('reject', 'Tidak Sesuai')])
    jenis_bahan = fields.Selection(string='Jenis Bahan', selection=[('pass', 'Sesuai'),
                                                                    ('reject', 'Tidak Sesuai')])
    ukuran_dimensi = fields.Selection(string='Ukuran / Dimensi', selection=[('pass', 'Sesuai'),
                                                                            ('reject', 'Tidak Sesuai')])
    kosmetika_name = fields.Selection(string='Nama Kosmetika', selection=[('pass', 'Sesuai'),
                                                                          ('reject', 'Tidak Sesuai')])
    batch_number = fields.Selection(string='Nomor Batch', selection=[('pass', 'Sesuai'),
                                                                     ('reject', 'Tidak Sesuai')])
    production_country = fields.Selection(string='Nama & Negara Produsen', selection=[('pass', 'Sesuai'),
                                                                                      ('reject', 'Tidak Sesuai')])
    customer_address = fields.Selection(string='Nama & Alamat Pemohon', selection=[('pass', 'Sesuai'),
                                                                                   ('reject', 'Tidak Sesuai')])
    utility = fields.Selection(string='Kegunaan', selection=[('pass', 'Sesuai'),
                                                             ('reject', 'Tidak Sesuai')])
    user_guide = fields.Selection(string='Cara Penggunaan', selection=[('pass', 'Sesuai'),
                                                                       ('reject', 'Tidak Sesuai')])
    expiration_date = fields.Selection(string='Tanggal Kadaluarsa', selection=[('pass', 'Sesuai'),
                                                                               ('reject', 'Tidak Sesuai')])
    composition = fields.Selection(string='Komposisi', selection=[('pass', 'Sesuai'),
                                                                  ('reject', 'Tidak Sesuai')])
    warning_text = fields.Selection(string='Peringatan & Keterangan', selection=[('pass', 'Sesuai'),
                                                                                 ('reject', 'Tidak Sesuai')])
    save_condition = fields.Selection(string='Kondisi Penyimpanan', selection=[('pass', 'Sesuai'),
                                                                               ('reject', 'Tidak Sesuai')])
    product_desc = fields.Many2one('product.template', string='Product')
    
    incoming_prod = fields.Float(string='Barang Datang')
    sample_qty  = fields.Float(string='Sample yang di ambil')
    reject_qty = fields.Float(string='Sampel yang Reject')
    
    sampling_operator = fields.Char(string='Petugas Sampling')
    mengetahui = fields.Char(string='Mengetahui')
    pemeriksa = fields.Char(string='Petugas Pemeriksa')
    
    note = fields.Text(string='Note')

    
    
    @api.model
    def create(self,vals):
        vals = vals
        name = self.env['ir.sequence'].next_by_code('self.qc.docs.bj')
        if vals['name'] == 'New':      
            vals.update({'name' : name})
        result = super(ADRBahanJadi, self).create(vals)
        return result

               

        

        

    