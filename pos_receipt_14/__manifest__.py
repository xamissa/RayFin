# -*- coding: utf-8 -*-

{
    'name': "POS Receipt Customisation",
    'summary': "POS Receipt Customisation",
    'description': """
        POS Receipt Customisation
    """,
    'category': '',
    'version': '14.0.1',
    'depends': ['pos_restaurant'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/pos_details_wizard_view.xml',
        'views/pos_receipt.xml',
        'views/report_pos_sale_details.xml',
        'views/pos_sale_view.xml',
    ],
    'qweb': ['static/src/xml/pos_ticket_view.xml'],
    'installable': True,
    'application': True,
}
