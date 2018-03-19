# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'DJ set - Accounting compilation for payment modes',
    'summary': "Create accounting songs from scratch",
    'version': '11.0.1.0.0',
    'author': 'Camptocamp,Odoo Community Association (OCA)',
    'maintainer': 'Camptocamp',
    'license': 'AGPL-3',
    'category': 'songs',
    'depends': ['dj_compilation_account', 'account_payment_mode'],
    'website': 'www.camptocamp.com',
    'data': ['data/dj.xml'],
    'test': [],
    'external_dependencies': {
    },
    'installable': True,
    'auto_install': True,
}
