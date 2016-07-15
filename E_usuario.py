from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy. import Column, Interger, String, Datatime, Boolean

base = declarative_base()
class usuario(object):
	tablename__= "usuario"	
	id= Column()
	nombre= Column()
	active= Column()
	password= Column()
	create_uid= Column()
	email= Column()
	write_date= Column()

	def __init__(self,id,nombre,active,password,create_uid,email,write_date):
		self.id=id
		self.nombre=nombre
		self.active=active
		self.password=password
		self.create_uid=create_uid
		self.email=email
		self.write_date=write_date
