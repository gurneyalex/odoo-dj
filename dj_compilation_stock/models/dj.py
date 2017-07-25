# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import fields, models


class DJCompilation(models.Model):
    _inherit = 'dj.compilation'

    genre = fields.Selection(selection_add=[('stock', 'Stock')])