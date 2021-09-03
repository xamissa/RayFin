# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _

import logging
_logger = logging.getLogger(__name__)


class PosOrder(models.Model):
    _inherit = "pos.order"

    @api.model
    def _order_fields(self, ui_order):
        note=''
        if ui_order['lines']:
            for l in ui_order['lines']:
                note = l[2]['note']
        res = super(PosOrder, self)._order_fields(ui_order)
        res['note'] = note
        return res
