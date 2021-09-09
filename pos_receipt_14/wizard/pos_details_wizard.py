# -*- coding: utf-8 -*-
from odoo import api, models, tools,fields,_
import logging
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

try:
    import xlsxwriter
except ImportError:
    _logger.debug('Can not import xlsxwriter`.')

class PosSaleDetailsWizard(models.TransientModel):
    _name = 'pos.sale.details.wizard'
    _description = 'Pos Sale Details Report'

    #start_date = fields.Date(string='Start Date', default=fields.Date.today())
    #end_date = fields.Date(string='End Date', default=fields.Date.today())
    start_date = fields.Datetime(required=True, string='Start Date', default=fields.Datetime.now)
    end_date = fields.Datetime(required=True, string='End Date', default=fields.Datetime.now)

    def print_pdf(self):
        print(">>>>......pppppppppeeeeeeeeeee")
        data = {'start_date': self.start_date, 'end_date': self.end_date}
        print("data:::::::::::::::::::::::::",data)
        return self.env.ref('pos_receipt_14.action_pos_sale_details_report').report_action([],data=data)
       

