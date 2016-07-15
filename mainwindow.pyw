import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QDialog
from PyQt5 import uic
from form_profesionales import Ui_form_profesionales
from form_actualizarproducto import Ui_form_actualizarproducto
from form_actualizarprofesionales import Ui_form_actualizarprofesionales
from form_borrarproducto import Ui_form_borrarproducto
from form_borrarprofesionales import Ui_form_borrarprofesionales
from form_buscarproducto import Ui_form_buscarproducto
from form_buscarprofesionales import Ui_form_buscaprofesionales
from form_contratos import Ui_form_Contratos
from form_contratosbuscar import Ui_form_contratosbuscar
from form_contratosgenerarconsumos import Ui_form_contratosgenerarconsumos
from form_producto import Ui_form_producto
from form_serviciodecontratos import Ui_form_serviciodecontratos
from form_usuarioborrar import Ui_form_usuarioborrar
from from_contratosgenerarfacturas import Ui_form_contratosgenerarfacturas
from form_usuarionuevo import Ui_form_usuarionuevo

#from PyQt5.QtCore import pyqtRemoveInputHook

class Mainwindow(QMainWindow):
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("mainwindow.ui", self)
        self.actionAgregar_Profesional.triggered.connect(self.Agregar_Profesional)
        self.actionAcutalizar_profesional.triggered.connect(self.Acutalizar_Profesional)
        self.actionBorrar_Profesional.triggered.connect(self.Borrar_Profesional)
        self.actionBuscar_Profesional.triggered.connect(self.Buscar_Profesional)

        self.actionBuscar_Productos.triggered.connect(self.Buscar_Productos)
        self.actionNuevo_Producto.triggered.connect(self.Nuevo_Producto)
        self.actionBorrar_Producto.triggered.connect(self.Borrar_Producto)
        self.actionActualizar_Productos.triggered.connect(self.Actualizar_Productos)

        self.actionNuevo_Contrato.triggered.connect(self.Nuevo_Contrato)
        self.actionBuscar_Contrato.triggered.connect(self.Buscar_Contrato)
        self.actionGenerar_Facturas.triggered.connect(self.Generar_Facturas)
        self.actionGenerar_Consumo.triggered.connect(self.Generar_Consumo)
        self.actionServicios_de_contratos.triggered.connect(self.Servicios_de_contratos)
        #self.actionNueva_Factura.triggered.connect(self.Nueva_Factura)
        #self.actionBuscar_Factura.triggered.connect(self.Buscar_Factura)
        #self.actionActualizar_Factura.triggered.connect(self.Actualizar_Factura)
        #self.actionBorrar_Factura.triggered.connect(self.Borrar_Factura)

        self.actionNuevo_Usuario.triggered.connect(self.Nuevo_Usuario)
        self.actionBorrar_Usuario.triggered.connect(self.Borrar_Usuario)

    def Agregar_Profesional(self):
        #from pdb4qt import set_trace; set_trace()
       #pyqtRemoveInputHook()
       # import pdb; pdb.set_trace()
        self.form_profesionales=QDialog()
        self.ui=Ui_form_profesionales()
        self.ui.setupUi(self.form_profesionales)
        self.form_profesionales.show()

    def Acutalizar_Profesional(self):
        self.form_actualizarprofesionales=QDialog()
        self.ui=Ui_form_actualizarprofesionales()
        self.ui.setupUi(self.form_actualizarprofesionales)
        self.form_actualizarprofesionales.show()

    def Borrar_Profesional(self):
        self.form_borrarprofesionales=QDialog()
        self.ui=Ui_form_borrarprofesionales()
        self.ui.setupUi(self.form_borrarprofesionales)
        self.form_borrarprofesionales.show()

    def Buscar_Profesional(self):
        self.form_buscarprofesionales=QDialog()
        self.ui=Ui_form_buscaprofesionales()
        self.ui.setupUi(self.form_buscarprofesionales)
        self.form_buscarprofesionales.show()

    #metodos producto
    def Buscar_Productos(self):
        self.form_buscarproducto=QDialog()
        self.ui=Ui_form_buscarproducto()
        self.ui.setupUi(self.form_buscarproducto)
        self.form_buscarproducto.show()

    def Nuevo_Producto(self):
        self.form_producto=QDialog()
        self.ui=Ui_form_producto()
        self.ui.setupUi(self.form_producto)
        self.form_producto.show()

    def Borrar_Producto(self):
        self.form_borrarproducto=QDialog()
        self.ui=Ui_form_borrarproducto()
        self.ui.setupUi(self.form_borrarproducto)
        self.form_borrarproducto.show()

    def Actualizar_Productos(self):
        self.form_actualizarproducto=QDialog()
        self.ui=Ui_form_actualizarproducto()
        self.ui.setupUi(self.form_actualizarproducto)
        self.form_actualizarproducto.show()

    #metodos contratos
    def Buscar_Contrato(self):
        self.lala=QDialog()
        self.ui=Ui_form_contratosbuscar()
        self.ui.setupUi(self.lala)
        self.lala.show()

    def Nuevo_Contrato(self):
        self.lala=QDialog()
        self.ui=Ui_form_Contratos()
        self.ui.setupUi(self.lala)
        self.lala.show()

    def Servicios_de_contratos(self):
        self.lala=QDialog()
        self.ui=Ui_form_serviciodecontratos()
        self.ui.setupUi(self.lala)
        self.lala.show()


    def Generar_Facturas(self):
        self.lala=QDialog()
        self.ui=Ui_form_contratosgenerarfacturas()
        self.ui.setupUi(self.lala)
        self.lala.show()

    def Generar_Consumo(self):
        self.lala=QDialog()
        self.ui=Ui_form_contratosgenerarconsumos()
        self.ui.setupUi(self.lala)
        self.lala.show()


    #metodos factura
    def Nueva_Factura(self):
        self.lala=QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.lala)
        self.lala.show()

    #def Buscar_Factura(self):
     #   self.lala=QDialog()
      #  self.ui=Ui_Dialog()
       # self.ui.setupUi(self.lala)
       # self.lala.show()

    def Actualizar_Factura(self):
        self.lala=QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.lala)
        self.lala.show()

    def Borrar_Factura(self):
        self.lala=QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.lala)
        self.lala.show()

        #usuarios
    def Nuevo_Usuario(self):
        self.form_usuarionuevo=QDialog()
        self.ui=Ui_form_usuarionuevo()
        self.ui.setupUi(self.form_usuarionuevo)
        self.form_usuarionuevo.show()

    def Borrar_Usuario(self):
        self.form_usuarioborrar=QDialog()
        self.ui=Ui_form_usuarioborrar()
        self.ui.setupUi(self.form_usuarioborrar)
        self.form_usuarioborrar.show()

app = QApplication(sys.argv)
_ventana = Mainwindow()
_ventana.show()
app.exec_()

