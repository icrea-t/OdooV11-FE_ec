# -*- coding: utf-8 -*-
{
    'name': "Ecuador's SRI",
    'summary': """Incluye todas las funcinalidades del SRI.""",
    'version': '9.0.4.0.1',
    'author': "Fabrica de Software Libre,Odoo Community Association (OCA)",
    'maintainer': 'Fabrica de Software Libre',
    'website': 'http://www.libre.ec',
    'license': 'AGPL-3',
    'category': 'Account',
    'depends': [
        'base',
        'account',
        'account_tax_python',
        'account_invoice_refund_link',
    ],
    'external_dependencies': {
        'python': [
            'stdnum',
            'xmltodict',
        ]
    },
    'data': [
        'views/account_fiscal_position.xml',
        'views/account_invoice.xml',
        'views/account_journal.xml',
        'views/account.xml',
        'views/account_payment.xml',
        'views/tax_form.xml',
        'views/autorizacion.xml',
        'views/comprobante.xml',
        'views/identificacion.xml',
        'views/persona.xml',
        'views/sustento.xml',
        'views/autorizacion.xml',
        'views/res_partner.xml',
        'views/res_users.xml',
        'views/res_company.xml',
        'views/report_account_invoice.xml',
        "data/sri/account.account.tag.csv",
        'data/sri/ats/l10n_ec_sri.tipopago.csv',
        'data/sri/ats/l10n_ec_sri.formapago.csv',
        'data/sri/ats/l10n_ec_sri.comprobante.csv',
        'data/sri/ats/l10n_ec_sri.sustento.csv',
        'data/sri/ats/l10n_ec_sri.identificacion.csv',
        'data/sri/ats/l10n_ec_sri.persona.csv',
        "data/sri/103/account.account.tag.csv",
        "data/sri/103/account.tax.group.csv",
        "data/sri/103/account.tax.csv",
        "data/sri/104/account.account.tag.csv",
        "data/sri/104/account.tax.group.csv",
        "data/sri/104/account.tax.csv",
        "data/sri/101/account.tax.group.csv",
        "data/sri/101/account.account.tag.csv",
        "data/sri/101/account.tax.csv",
        "data/account/account.fiscal.position.csv",
        "wizards/account_invoice_view.xml",
        "data/menus.xml",
        "data/res_country_data.xml",
        # "data/res_lang_data.xml",
        "security/ir.model.access.csv",
    ],
    'demo': [],
    'test': [],
    'installable': True,
}