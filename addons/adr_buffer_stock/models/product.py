from odoo import models, fields, api
from datetime import date
from io import StringIO
import base64

class Product(models.Model):
    _inherit = ['product.template']

    qty_low_stock_notify = fields.Integer(string='Notify for Qty Below', default=80,
                                          help='When stock on hand falls below this number, it will be included in the low stock report. Set to -1 to exclude from the report.')

    @api.model
    def send_low_stock_via_email(self):
        header_label_list=["SKU", "Name", "Qty On Hand","Qty Incoming","Low Stock Qty"]
        ## Get email template
        template_obj = self.env['mail.template']
        template_ids = template_obj.search([('name', '=', 'Low Stock Automated Report')])
        template     = template_ids
        if template:
            default_body = template.body_html
            custom_body  = """
                <h3>Low Stock Notification</h3>
                <p>Dear Andara Team, berikut terlampir beberapa product Low Stock</p>
                <hr> 
                <table>
                    <th style="width:100px;">%s</th>
                    <th style="width:200px;">%s</th>
                    <th style="text-align:center;width:100px;">%s</th>
                    <th style="text-align:center;width:100px;">%s</th>
                    <th style="text-align:center;width:100px;">%s</th>
            """ %(header_label_list[0], header_label_list[1], header_label_list[2], header_label_list[3], header_label_list[4])
            ## Check for low stock products
            product_obj  = self.env['product.product']
            product_ids  = product_obj.search([('active', '=', True), ('sale_ok', '=', True), ('default_code', '!=', False)])
            for product in product_ids:
                product_sku = product.default_code
                if not product_sku or product_sku == '':
                    continue
                qty_available = product.qty_available
                qty_incoming  = product.incoming_qty
                qty_low_stock_notify = product.qty_low_stock_notify
                if qty_available <= qty_low_stock_notify and qty_low_stock_notify >= 0: 
                    # template_obj.send_mail()                  
                    custom_body += """    
                        <tr style="font-size:14px;">
                            <td>%s</td>
                            <td>%s</td>
                            <td style="text-align:center;">%s</td>
                            <td style="text-align:center;">%s</td>
                            <td style="text-align:center;">%s</td>
                        </tr>
                    """ %(product_sku, product.name, str(qty_available), str(qty_incoming), str(qty_low_stock_notify))
            custom_body  += "</table>"
            footer = """
                <hr>
                <br>
                <strong>** Email ini di generate otomatis melalui Sistem</strong>"""
            template.body_html = default_body + custom_body + footer
            partner = self.env['res.partner'].search([('email', '!=', '')]).ids
            list_mail = []
            for mail in partner:
                email = self.env['res.partner'].browse(mail)
                list_mail.append(email.email)
            position = 0  
            for send in list_mail:
                queue = list_mail[position]                          
            vals = {
                    'subject': 'Andara Low Stock',
                    'body_html': template.body_html,
                    'email_to': 'baydevincent@gmail.com',
                    'email_cc': '',
                    'auto_delete': False,
                    'email_from': 'baydevincent@gmail.com',
                    }
            mail_id = self.env['mail.mail'].sudo().create(vals)
            mail_id.sudo().send()
            position = position + 1
            # send_email         = mail_obj.template_obj.with_context(force_send=True).message_post_with_template(template_ids)
            template.body_html = default_body
            return True
