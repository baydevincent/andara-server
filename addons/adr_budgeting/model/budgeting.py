'''
Created on Mar 08, 2023

@author: BYDEV
'''

from odoo import api, fields, models, _
from odoo.exceptions import UserError,Warning


class ADRBudgeting(models.Model):
    _name = "adr.budgeting"
    _description = "Andara Monthly Budgeting"
                
    name = fields.Char(string='Order Reference', required=True, copy=False, states={'draft': [('readonly', False)]}, index=True, default=lambda self: _('New'))
    responsible_id = fields.Many2one('res.users', string='Responsible', required=True, states={'done': [('readonly', True)], 'confirmed': [('readonly', True)]})
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    date_order = fields.Datetime(string='Tanggal Order', 
                                 required=True, readonly=True, index=True, 
                                 states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, 
                                 copy=False, default=fields.Datetime.now)
    is_locked = fields.Boolean(string="locked", readonly=True, default=False)   
    planned_expenses = fields.Float(string='Expenses Planned', readonly=True) #, compute='_amount_planned_income'
    planned_income = fields.Float(string='Income Planned', readonly=True)
    actual_expenses = fields.Float(string='Actual Expenses', readonly=True)
    actual_income = fields.Float(string='Actual Income', readonly=True)
    expenses_line = fields.Many2many('expense.line', states={'done': [('readonly', True)], 'confirmed': [('readonly', True)]})
    income_line = fields.Many2many('incomes.line', states={'done': [('readonly', True)], 'confirmed': [('readonly', True)]})
    validator = fields.Many2one('res.users', string="Confirmed By", readonly=True)
    
    @api.model
    def create(self,vals):
        vals = vals
        name = self.env['ir.sequence'].next_by_code('self.budget')
        if vals['name'] == 'New':      
            vals.update({'name' : name})
        result = super(ADRBudgeting, self).create(vals)
        return result
    
    # def check_lock(self):
        # if self.is_locked == True:
            # raise UserError("Maaf Budget sudah terkunci")
        # return True
               
    def sum_planned_expenses(self):
        for order in self:
            plan_expense = 0.0
            plan_income = 0.0
            actual_expenses = 0.0
            actual_income = 0.0
            for line in order.expenses_line:
                plan_expense += line.planned
                actual_expenses += line.actual
                line.update({
                        'diff' : line.planned - line.actual
                        })
                if line.budget_id == 0:
                    line.update({
                        'budget_id' : order.id
                        })
                    
            for line2 in order.income_line:
                plan_income += line2.planned
                actual_income += line2.actual
                line2.update({
                        'diff' : line2.planned - line2.actual
                        })
                if line2.income_id == 0:
                    line2.update({
                        'income_id' : order.id
                        }) 
                          
            order.update({
                    'planned_expenses'  : plan_expense,
                    'actual_expenses'   : actual_expenses,
                    'planned_income'    : plan_income,
                    'actual_income'   : actual_income,
                })
            
    def lock_budget(self):
        self.update({
                'is_locked' : True,
            })
    
    def confirm_budget(self):
        self.update({
                'state' : 'confirmed',
                'validator' : self.env.user
            })
        return True
    
    def set_draft(self):
        self.update({
                'state' : 'draft',
            })
        return True
    
    def unlock_budget(self):
        self.update({
                'state' : False,
            })
     
        
class ExpensesLine(models.Model):
    _name = 'expense.line'
    _description = "Budgeting Form"
        
    budget_id = fields.Integer(string='budget id', readonly=True)
    # currency_id = fields.Many2one(string='Valuta', store=True, default=1) ##depends=["pricelist_id"],
    category = fields.Char(string='Category', default='-')
    planned = fields.Float(string='Planned')
    actual = fields.Float(string='Actual')
    diff = fields.Float(string='Different', readonly=True)
    
    
class IncomeLine(models.Model):
    _name = 'incomes.line'
    _description = "Budgeting Form"
    
    income_id = fields.Integer(string='income id',readonly=True)
    # currency_id = fields.Many2one(string='Valuta', store=True, default=1) ##depends=["pricelist_id"],
    category = fields.Char(string='Category')
    planned = fields.Float(string='Planned')  
    actual = fields.Float(string='Actual')
    diff = fields.Float(string='Different',readonly=True)
        

    