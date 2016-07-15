import sys 
#import datetime
#from N_profesionales import N_datos_academicos
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean
#from coneccion import Coneccion
from PyQt5.QtCore import pyqtRemoveInputHook

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class E_datos_academicos(Base):
    __tablename__="datos_academicos"
    id= Column(Integer, primary_key=True)
    id_party = Column(Integer)
    universidad = Column(String)
    fecha_titulo = Column(DateTime, default=func.now())
    fecha_min = Column(DateTime, default=func.now())
    fecha_mej = Column(DateTime, default=func.now())
    titulo = Column(String)

    def __init__(self,id,id_party):
        self.id=id
        self.id_party= id_party

    #def __init__(self,_id,_id_party,universidad,fecha_titulo,fecha_min,nombre,fecha_mej,titulo):
     #   self.id=_id
     #   self.id_party=_id_party
      #  self.universidad=universidad
       # self.fecha_titulo=fecha_titulo
       # self.fecha_min=fecha_min
       # self.fecha_mej=fecha_mej
       # self.titulo= titulo

    def guardar(self, list_N_datos_academicos):
        #Session= Coneccion()
        engine=create_engine('postgresql://postgres:postgres@localhost:5432/psicologos')
        Session= sessionmaker(bind=engine) 
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        session=Session()

        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        for item in list_N_datos_academicos: 
            new_record = E_datos_academicos(1,1)
            new_record.universidad =item.universidad
            new_record.fecha = item.fecha_titulo
            new_record.fecha_min = item.fecha_min
            new_record.fecha_mej = item.fecha_mej
            new_record.titulo = item.titulo

            session.add(new_record)
            session.commit()
        
        all_records = session.query(E_datos_academicos).all()
        
        return all_records

