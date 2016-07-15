from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Datetime,Boolean

Base = declarative_base()
class party_profesional(object):
	__tablename__="party_profesional"
	id= Column(Integer, primary_key=True)
	id_party= Column(Integer)
	estado_civil = Column(String(100))
	nacionalidad =  Column(String(100))
	fecha_nac = Column(Datetime)
	lugar =  Column(String(100))
	nro_legajo = Column(String(50))

	def __init__(self,id,id_party,estado_civil,nacionalidad,fecha_nac,lugar,nro_legajo):
		self.id=id
		self.id_party=id_party
		self.estado_civil=estado_civil
		self.nacionalidad=nacionalidad
		self.fecha_nac=fecha_nac
		self.lugar=lugar
		self.nro_legajo=nro_legajo
