# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class multimedia(osv.osv):
    _name ='ci.multimedia'
    _description= 'CO Multimedia'
    _rec_name="title"
    _order="release_date desc"
    
    def _computer_stock(self,cr,uid,ids,field_name,arg,context):
         stock_obj=self.pool.get('co.lineas.stock')
         res={}
         if isinstance(ids,(int,long)):
            ids=[ids]
         for i in ids:
            lineas_ids=stock_obj.search(cr,uid,[('mutimendia_id','=',i),])
            lineas_brw=stock_obj.browse(cr,uid,lineas_ids)
            res[i]=sum([l.quantity for l in lineas_brw])
            
         return res
        
    _columns={
    'cade':fields.char('Código'),
    'title':fields.char('Titulo', required=True),
    'release_date':fields.date('Fecha de Publicación'),
    'categoria_id':fields.many2one('co.categoria','Categoria'),
    'medios_ids':fields.many2many(
        'co.tipo.medio',
        'co_muntimedia_tipo_medio_rel',
        'multimedia_id',
        'medio_id'),
    'stock':fields.function(_computer_stock,type='integer'),
    }
    
multimedia()
