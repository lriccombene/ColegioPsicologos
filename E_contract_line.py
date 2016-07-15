from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Datetime,Boolean

Base = declarative_base()
class contract_line(object):
	__tablename__="datos_academicos"
	id= Column(Integer, primary_key=True)
	create_uid = Column(Datetime)
	create_date = Column(Datetime)
	descripcion = Column(String())
	id_servicio = Column(Integer)
	fecha_inicio = Column(Datetime)
	fecha_fin = Column(Datetime)
	precio_unitario = Column(Datetime)
	id_contrato = Column(Integer)

	def __init__(self,_id,create_uid,create_date,descripcion,id_servicio,fecha_inicio,fecha_fin,precio_unitario,id_contrato):
		self.id=_id
		self.create_uid=create_uid
		self.create_date=create_date
		self.descripcion=descripcion
		self.id_servicio=id_servicio
		self.fecha_inicio=fecha_inicio
		self.fecha_fin=fecha_fin
		self.precio_unitario=precio_unitario
		self.id_contrato=id_contrato
