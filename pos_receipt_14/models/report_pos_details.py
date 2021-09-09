# -*- coding: utf-8 -*-
from odoo import api,models,fields, _
import time
import datetime
from datetime import date
from odoo.osv import osv
import logging

_logger = logging.getLogger(__name__)

class ReportPosSaleDetails(models.AbstractModel):

    _name = 'report.pos_receipt_14.report_pos_details'
    _description = 'POS sale Details'

    @api.model
    def get_pos_sale_details(self, start_date=False, end_date=False, config_ids=False, session_ids=False):
        print("get_pos_sale_details==================",(start_date))

        if start_date:
            start_date = fields.Datetime.from_string(start_date)
        else:
            # start by default today 00:00:00
            user_tz = pytz.timezone(self.env.context.get('tz') or self.env.user.tz or 'UTC')
            today = user_tz.localize(fields.Datetime.from_string(fields.Date.context_today(self)))
            start_date = today.astimezone(pytz.timezone('UTC'))

        if end_date:
            end_date = fields.Datetime.from_string(end_date)
            # avoid a end_date smaller than start_date
            if (end_date < start_date):
                end_date = start_date + timedelta(days=1, seconds=-1)
        else:
            # stop by default today 23:59:59
            end_date = start_date + timedelta(days=1, seconds=-1)

        print("start_date::::::::::::::::;;",start_date,end_date)
        order_ids = self.env['pos.order'].sudo().search([('date_order', '>=', fields.Datetime.to_string(start_date)),('date_order', '<=', fields.Datetime.to_string(end_date))
            ])

        user_currency = self.env.company.currency_id

        lines = {}
        total = 0.0
        print("order_ids===>>",order_ids)
        for order in order_ids:
            dict1 = {}
            dict2 = {}
            for line in order.lines:
                print("line::::::",line)
                total += line.price_subtotal_incl
                dict1[line.id] = {
                            'product_id' : line.product_id.id,
                            'product_name' : line.product_id.name,
                            'order_ref' : line.order_id.name,
                            'customer' : line.order_id.partner_id.name,
                            'receipt_ref' : line.order_id.pos_reference,
                            'session' : line.order_id.session_id.name,
                            'note' : line.note,
                            'qty' : line.qty,
                            'unit_price' : line.price_unit,
                            'subtotal' : line.price_subtotal_incl,
                        }
                print("dict1:<<<<<<<<<<<<",dict1)
                lines.update(dict1)
        
        print("lines::::::::::::::::",lines)    
        return {
            'currency_precision': user_currency.decimal_places,
            'total': total,
            'lines': lines,
        }


    @api.model
    def _get_report_values(self, docids, data=None):
        print("_get_report_values>>>>>>>>>>>>>>>>>>>>",data)
        data = dict(data or {})
        data.update(self.get_pos_sale_details(data['start_date'], data['end_date']))
        print("dataddddddddd:::::::::::",data)
        return data

