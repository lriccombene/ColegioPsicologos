from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy. import Column, Interger, String, Datatime, Boolean

base = declarative_base()
class areas_profesionales(areas_profesionales):
	tablename__= "areas_profesionales"	
	id= Column()
	descripcion= Column()

	def __init__(self,id,descripcion):
	self.id = id
	self.descripcion = descripcions