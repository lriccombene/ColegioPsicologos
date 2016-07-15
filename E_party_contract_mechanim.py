from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Datetime,Boolean

Base = declarative_base()
class party_contrat_mechanim(object):
	__tablename__="party_contrat_mechanim"
	id= Column(Integer, primary_key=True)
	comment = Column(String())
	create_uid = Column(Datetime)
	create_date = Column(Datetime)
	value = Column(Integer)
	write_date  = Column(Datetime)
	activo =Column(Boolean)
	id_party = Column(Integer)
	type_contacto = Column(String(100))

	def __init__(self,id,id_party,comment,create_uid,create_date,value,write_date,activo,type_contacto):
		self.id=id
		self.id_party=id_party
		self.comment=comment
		self.create_uid=create_uid
		self.create_date=create_date
		self.value=value
		self.write_date=write_date
		self.activo=activo
		self.type_contacto= type_contacto
