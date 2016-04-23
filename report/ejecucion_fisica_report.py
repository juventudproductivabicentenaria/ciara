# -*- coding: utf-8 -*-

import time
from openerp.report import report_sxw
import datetime
import openerp.pooler
from openerp.osv import osv, fields


class ejecucion_fisica(report_sxw.rml_parse):
    

    def __init__(self, cr, uid, name, context):
        super(ejecucion_fisica,self).__init__(
            cr,uid,name,context=context)
        self.total = []    
        self.localcontext.update({
        'time': time,
        #~ 'suma': suma,
        #~ 'suma_total' : self.suma_total,
        'get_total': self.gettotal,
        'get_data': self.get_data,
        'organizacion_data':self.organizacion_data,
        'materiales_apoyo_data':self.materiales_apoyo_data,
        'acciones_especificas_data':self.acciones_especificas_data,
        'tecnico_data':self.tecnico_data,
        'fundo_data':self.fundo_data,
        #~ 'ejecucion_fisica_data':self.ejecucion_fisica_data,
        })
        self.familias_atendidas = 0.0
        

    def get_data(self,date_start,date_end):
        tids = self.pool.get('ejecucion_fisica').search(self.cr,self.uid,[('fecha_planificacion', '>=', date_start),('fecha_ejecucion', '<=', date_end)])
        res = self.pool.get('ejecucion_fisica').browse(self.cr,self.uid,tids)
        return res
        
    def organizacion_data(self,ejecucion_fisica):
        organizacion_str=''
        for m in ejecucion_fisica.organizacion_id:
             organizacion_str +="%s , %s" % (m.nombre,organizacion_str)
        return organizacion_str 
     
        
    def materiales_apoyo_data(self,ejecucion_fisica):
        materiales_apoyo_str=''
        for d in ejecucion_fisica.materiales_apoyo_ids:
             materiales_apoyo_str +="%s , %s" % (d.nombre,materiales_apoyo_str)
        return materiales_apoyo_str 
     
    def ejecucion_fisica_data(self,ejecucion_fisica):
        ejecucion_fisica_str=''
        for d in ejecucion_fisica.ejecucion_fisica_id:
             ejecucion_fisica_str +="%s , %s" % (d.resultado,ejecucion_fisica_str)
        return ejecucion_fisica_str  
        
    def acciones_especificas_data(self,ejecucion_fisica):
        acciones_especificas_str=''
        for w in ejecucion_fisica.acciones_especificas_id:
             acciones_especificas_str +="%s , %s" % (w.objetivo,acciones_especificas_str)
        return acciones_especificas_str     
        
    def tecnico_data(self,creador):
        print str(creador[0])
        return creador[0]
        
    def fundo_data(self,ejecucion_fisica): 
        fundo_str=''
        for w in ejecucion_fisica.fundo_id:
             fundo_str +="%s , %s" % (w.nombre,fundo_str)
        return fundo_str   
                
    def gettotal(self,ejecucion_fisica,total):
        self.ejecucion_fisica = self.ejecucion_fisica + int(total)
        return total
        
    def suma_total(self, ejecucion_fisica):
        return res
        

report_sxw.report_sxw('report.ejecucion_fisica.familias_atendidas','ejecucion_fisica','addons/ciara_fz/report/ejecucion_fisica_report.rml',parser=ejecucion_fisica)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
