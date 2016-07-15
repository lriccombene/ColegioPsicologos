#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5 import uic
from form_contratosgenerarfacturas import Ui_form_contratosgenerarfacturas


obj_dte_fecha_facturas_generadas=""
obj_form_contratosgenerarfacturas = Ui_form_contratosgenerarfacturas()


class Dialogo(QDialog):
        def __init__(self):
                QDialog.__init__(self)
               #self.obj_form_contratosgenerarfacturas = Ui_form_contratosgenerarfacturas()
        		self.obj_form_contratosgenerarfacturas.setupUi(self)
        		self.obj_dte_fecha_facturas_generadas=self.obj_form_contratosgenerarfacturas.dte_fecha_facturas_generadas.value()
        		self.obj_form_contratosgenerarfacturas.boton_generar.clicked.connect(self.Guardar)

        def Guardar(self):
        	self.obj_dte_fecha_facturas_generadas=self.obj_form_contratosgenerarfacturas.dte_fecha_facturas_generadas.value()
        	




app = QApplication(sys.argv)
dialogo= Dialogo()
dialogo.show()
app.exec_()
