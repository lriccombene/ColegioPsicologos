import sys
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5 import uic
from form_producto import Ui_form_producto

class Dialogo(QDialog):
    nombre = ""
    categoria = ""
    precio_lista = 0.0
    precio_costo = 0.0
    unidad_medida = ""
    consumible = False
    vendible = False
    comprable = False
    tipo = ""
    form_productos=Ui_form_producto()

    def __init__(self):
        QDialog.__init__(self)
        self.form_productos = Ui_form_producto()
        self.form_productos.setupUi(self)
        self.form_productos.boton_guardar.clicked.connect(self.guardar)

    def guardar(self):
        nombre= self.form_productos.lne_nombre.text()
        categoria = self.form_productos.cbx_categoria.currentText()
        precio_lista = self.form_productos.lne_precio_lista.text()
        precio_costo = self.form_productos.lne_precio_costo.text()
        unidad_medida = self.form_productos.cbx_unidad_medida.currentText()
        consumible = self.form_productos.ckbx_consumible.isChecked()
        vendible = self.form_productos.ckbx_vendible.isChecked()
        comprable = self.form_productos.ckbx_comprable.isChecked()
        tipo = self.form_productos.cbx_tipo.currentText()
        self.form_productos.resultado.setText(nombre)






app = QApplication(sys.argv)
dialogo= Dialogo()
dialogo.show()
app.exec_()
