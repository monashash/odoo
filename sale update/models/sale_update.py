from odoo import models, fields ,api
from datetime import date

class SaleUpdate(models.Model):
    _name = 'sale.update'
    _description = 'Sale Update'

    sale_id = fields.Many2one('sale.order', string='Sale Order', required=True)
    birth_date = fields.Date(string="Birth Date")
    current_date = fields.Date(string="Current Date", default=date.today())
    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], string='Status', default='draft')

    @api.depends('birth_date', 'current_date')
    def _compute_age(self):
        for person in self:
            if person.birth_date:
                birth_date = fields.Date.from_string(person.birth_date)
                current_date = fields.Date.from_string(person.current_date)
                delta = current_date - birth_date
                person.age = delta.days //365
 
    def action_confirm(self):
        self.state = 'confirmed'

    def action_done(self):
        self.state = 'done'

    def action_reset_to_draft(self):
        self.state = 'draft'
