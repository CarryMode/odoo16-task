from odoo import models, fields

class Company(models.Model):
    _name = "developers.management.company"
    _description = "Company"

    name = fields.Char(required=True)
    address = fields.Text()
    developers_ids = fields.One2many(
        comodel_name="developers.management.developer",
        inverse_name="company_id",
    )
