from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Datetime,Boolean

Base = declarative_base()
class party_address(object):
	__tablename__="party_party"
	id= Column(Integer, primary_key=True)
	ciudad = Column(String(100))
	create_date = Column(Datetime)
	nombre =Column(String(100))
	zip = Column(String(100))
	create_uid = Column(Datetime)
	subdivision =  Column(String(100))
	pais =  Column(String(100))
	street =	Column(String(100))
	id_party =  Column(Integer)


	def __init__(self, id, ciudad, create_date, nombre, zip, create_uid, subdivision, pais, street, id_party):
		super(party_party, self).__init__()
		 self.id = id
		 self.ciudad = ciudad
		 self.create_date =create_date
		 self.nombre = nombre
		 self.zip = zip
		 self.create_uid = create_uid
		 self.subdivision = subdivision
		 self.pais = pais
		 self.street = street
		 self.id_party = id_party
		 

