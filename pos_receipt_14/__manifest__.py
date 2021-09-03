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
        'views/pos_receipt.xml',
    ],
    'qweb': ['static/src/xml/pos_ticket_view.xml'],
    'installable': True,
    'application': True,
}
