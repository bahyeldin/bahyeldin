from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    completion_percentage = fields.Float(string="% of Completion", default=100)
    previous_qty = fields.Float(string="Previous qty")
    previous_percentage = fields.Float(string="Previous percentage")
    total_qty = fields.Float(string="total Qty")
    construction_id = fields.Many2one('account.move', string='Is a construction')
    comulative_invoice = fields.Float( string='cumulative Invoice', compute='_compute_comulative_invoice')

    construction = fields.Boolean(related='move_id.construction', store=True)






    @api.onchange('completion_percentage', 'quantity', 'price_unit')
    def _onchange_completion_percentage(self):
        if self.completion_percentage < 0 or self.completion_percentage > 100:
            raise ValidationError("Completion percentage must be between 0 and 100.")





    @api.depends('total_qty','price_unit','completion_percentage','construction')
    def _compute_comulative_invoice(self):
        for line in self:
         	   line.comulative_invoice = line.total_qty * line.price_unit * line.completion_percentage/100



    @api.onchange('total_qty','previous_qty','previous_percentage','completion_percentage','price_unit','construction')
    def _compute_quantity(self):
        for line in self:
         	   line.quantity = ((line.total_qty * (line.completion_percentage / 100)) - (line.previous_qty * line.previous_percentage/100 ))


    def action_set_previous_qty(self):
        for line in self:
            line.previous_qty = line.total_qty
            line.previous_percentage = line.completion_percentage



    def action_set_current_percentage(self):
        for line in self:

            line.quantity = ((line.total_qty * (line.completion_percentage / 100)) - (line.previous_qty * line.previous_percentage/100 ))





class AccountMove(models.Model):
    _inherit = 'account.move'

    construction = fields.Boolean(default=False, string='construction')

    inv_num_con = fields.Char(string='Construction Invoice Num')

    construction_ids = fields.One2many('account.move.line', 'construction_id', string='construction ids')
    construction_project_id = fields.Many2one('construction.projects',string='Construction Project')



class ConstructionProjects(models.Model):
    _name = 'construction.projects'
    _description = 'list of construction projects'


    name = fields.Char(string='project')













