from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy. import Column, Interger, String, Datatime, Boolean

base = declarative_base()
class actuacion_laboral(actuacion_laboral):
	tablename__= "actuacion_laboral"	
	id= Column()
	id_party= Column()
	ideareaprofesional= Column()

	def __init__(self,id,id_party, ideareaprofesional):
	self.id = id
	self.id_party = descripcions
	self.ideareaprofesional = ideareaprofesional