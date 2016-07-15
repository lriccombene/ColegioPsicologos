import sys
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5 import uic
from form_contratosbuscar import Ui_form_contratosbuscar
from N_contratosbuscar import Contratos


nombre = ""
profesional = ""
dte_mes_de_contrato="06/06/2016"


form_contratosbuscar = Ui_form_contratosbuscar()

class Dialogo(QDialog):
	def __init__(self):
      	QDialog.__init__(self)
        self.form_contratosbuscar.setupUi(self)
      	self.obj_form_contratosgenerarfacturas.boton_buscar.clicked.connect(self.Buscar)

    def Buscar(self):
    	nombre= self.form_contratosbuscar.lne_nombre.text()
        profesional= self.form_contratosbuscar.lne_profesional.text()
        dte_mes_de_contrato= self.form_contratosbuscar.dte_mes_de_contrato.text()
        contratos = Contratos()
        contratos.contratos_buscar(nombre,profesional,dte_mes_de_contrato)




app = QApplication(sys.argv)
dialogo= Dialogo()
dialogo.show()
app.exec_()
