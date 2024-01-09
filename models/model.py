from odoo import api, models

class CustomInvoiceReport():
    _name = 'your_module_name.custom_invoice_report'
    _inherit = 'account.move'