# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv
from openerp.tools import config
#~ import wizard

class ejecucion_fisica_report_wizard(osv.osv_memory):
    _name = "ejecucion_fisica.report.wizard"
   
    _rec_name = 'date_start'
    _columns = {
                'date_start':fields.datetime('fecha_planificacion'),
                'date_end':fields.datetime('fecha_ejecucion')
                }
    def print_report(self, cr, uid, ids, context=None):
        datas = {
             'ids': ids,
             'model': 'ciara_fz.ejecucion_fisica',
             'form': self.read(cr, uid, ids)[0]
        }
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'ejecucion_fisica.familias_atendidas',
            'datas': datas,
        }
         
         
ejecucion_fisica_report_wizard()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
