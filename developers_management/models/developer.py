from odoo import models, fields, api

class Developer(models.Model):
    _name = "developers.management.developer"
    _description = "Developer"

    _sql_constraints = [
        ("unique_name", "unique(name)", "Developer name must be unique!"),
    ]

    name = fields.Char(required=True)
    type = fields.Selection([
        ("front-end", "Front-end"),
        ("backend", "Backend"),
        ("fullstack", "Fullstack"),
        ("out-stuff", "Out-stuff"),
    ])
    global_identification = fields.Char(
        compute="_compute_global_identification",
        store=True,
    )
    phone = fields.Char()
    email = fields.Char()
    address = fields.Text()
    birth_date = fields.Date()
    job_position = fields.Char()
    company_id = fields.Many2one(
        comodel_name="developers.management.company",
    )

    @api.depends("name", "type")
    def _compute_global_identification(self):
        for record in self:
            if record.name and record.type:
                record.global_identification = f"{record.name}-{record.type}"
            else:
                record.global_identification = False
