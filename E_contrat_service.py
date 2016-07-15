from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy. import Column, Interger, String, Datatime, Boolean

base = declarative_base()
class cotrat_service(cotrat_service):
	tablename__= "cotrat_service"	
	id= Column()
	create_id= Column()
	product= Column()
	create_date= Column()
	name= Column()
	write_uid= Column()
	write_date= Column()

def __init__(self,id,create_id,product,create_date,write_uid,name,write_date):
		self.id = id
		self.create_id = create_id
		self.product = product
		self.create_date = create_date
		self.write_uid = write_uid
		self.name = name
		self.write_date = write_date