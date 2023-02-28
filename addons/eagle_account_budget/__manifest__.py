# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

{
    'name': 'Eagle 12 Budget Management',
    'author': 'Eagle Mates, Eagle SA',
    'category': 'Accounting',
    'description': """Use budgets to compare actual with expected revenues and costs""",
    'summary': 'Eagle 12 Budget Management',
    'website': 'http://eagle-erp.com',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'security/account_budget_security.xml',
        'views/account_analytic_account_views.xml',
        'views/account_budget_views.xml',
        'views/res_config_settings_views.xml',
    ],
    "images": ['static/description/banner.gif'],
    'demo': ['data/account_budget_demo.xml'],
}
