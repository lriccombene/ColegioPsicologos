from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmarker

class Coneccion(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(Coneccion, self).__init__()
        self.arg = arg

    def Conec(self):
        engine=create_engine('postgresql://postgres:postgres@localhost:5432/psicologos')
        Session= sessionmarker(bind=engine) 
        session=Session()
        return session