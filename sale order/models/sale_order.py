from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('first_approval', 'First Approval'),
        ('second_approval', 'Second Approval'),
        ('third_approval', 'Third Approval'),
        ('sale', 'Sale Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
    ], string='Status', copy=False, index=True, tracking=3, default='draft')

    so_type = fields.Selection([
        ('local', 'Local'),
        ('export', 'Export')
    ], string='SO Type', default='local')

    def approval_first_level(self):
        self.state = 'first_approval'

    def approval_second_level(self):
        self.state = 'second_approval'

    def approval_third_level(self):
        if self.state == 'second_approval' and self.so_type == 'export':
            self.state = 'third_approval'

    def action_confirm(self):
        if self.state == 'third_approval' or (self.state == 'second_approval' and self.so_type == 'local'):
            super(SaleOrder, self).action_confirm()

    @api.onchange('so_type')
    def _onchange_so_type(self):
        if self.so_type == 'local' and self.state == 'third_approval':
            self.state = 'second_approval'
        elif self.so_type == 'export' and self.state == 'second_approval':
            self.state = 'third_approval'


