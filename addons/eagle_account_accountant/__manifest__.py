# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

{
    'name': 'Eagle12 Accounting',
    'version': '12.0.3.2.0',
    'category': 'Accounting',
    'summary': 'Accounting Reports, Asset Management and Account Budget For Eagle12 Community Edition',
    'sequence': '8',
    'author': 'Eagle Mates, Eagle SA',
    'website': 'http://eagle-erp.com',
    'maintainer': 'Eagle Mates',
    'support': 'eagle.erp.com@gmail.com',
    'live_test_url': 'https://www.youtube.com/watch?v=Kj4hR7_uNs4',
    'website': '',
    'depends': ['accounting_pdf_reports', 'eagle_account_asset', 'eagle_account_budget'],
    'demo': [],
    'data': [
        'wizard/change_lock_date.xml',
        'views/account.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.gif'],
    'qweb': [],
}
