from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Datetime,Boolean

Base = declarative_base()
class party_party(object):
	__tablename__="party_party"
	id= Column(Integer, primary_key=True)
	code = Column(String(100))
	create_date = Column(Datetime)
	write_uid =Column(Integer(100))
	write_date = Column(Datetime)
	active =  Column(Boolean)
	nombre =  Column(String(100))
	apellido =  Column(String(100))
	tipo_doc =	Column(String(50))
	nro_doc =  Column(String(100))


	def __init__(self, id, code, create_date, write_uid, write_date, active, nombre, apellido, tipo_doc, nro_doc):
		super(party_party, self).__init__()
		 self.id = id
		 self.code = code
		 self.create_date =create_date
		 self.write_uid = write_uid
		 self.write_date = write_date
		 self.active = active
		 self.nombre = nombre
		 self.apellido = apellido
		 self.tipo_doc = tipo_doc
		 self.nro_doc = nro_doc
		 

