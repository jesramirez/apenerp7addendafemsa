# -*- encoding: utf-8 -*-
import openerp
from openerp import netsvc, tools, pooler
from openerp.osv import fields, osv
from openerp.tools.translate import _

class sale_order(osv.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'
    _columns = {
        'entrance':fields.char('Entrance', size=20, help="Number assigned by Femsa, for entering product to your stock"),
        'currency_local':fields.selection([('MXP','MXP'),
 		('USD','USD')],'Currency_local', help="Currency in which the sale was made"),
        'referral':fields.char('Referral', size=20, help="Number Referral sale"),
        'purchase_order':fields.char('Purchase Order', size=20, help="Purchase Order Number"),
        'consumption_order':fields.char('Consumption Order', size=20, help="Consumption Order Number"),
    }
 