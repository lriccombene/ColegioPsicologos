import sys
from PyQt5.QtWidgets import QApplication,QDialog, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from form_profesionales import Ui_form_profesionales
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5 import QtGui
from N_profesionales import N_datos_academicos ,N_datos_profesionales, N_datos_personales_prof,N_datos_bancarios

class Dialogo(QDialog):
    
    obj_form= Ui_form_profesionales()
    
    apellido = ""
    nombre = ""
    genero = ""
    list_titulos_prof=list()


    def __init__(self):
            QDialog.__init__(self)
            self.obj_form = Ui_form_profesionales()
            self.obj_form.setupUi(self)
            self.obj_form.boton_guardar.clicked.connect(self.guardar)
            self.obj_form.boton_agregar.clicked.connect(self.agregar)


    def guardar(self):
       
        
        apellido = self.obj_form.lne_apellido.text()
        nombre = self.obj_form.lne_nombre.text()
        genero = self.obj_form.cbx_genero.currentText()
        nac = self.obj_form.cbx_nacionalidad.currentText()
        tipo_doc = self.obj_form.cbx_tipo_doc.currentText()
        nro_doc = self.obj_form.lne_numero_doc.text()
        fec_nac = self.obj_form.dte_fecha_nacimiento.text()
        lugar_nac = self.obj_form.lne_lugar_nacimiento.text()
        estado_civil = self.obj_form.cbx_estado_civil.currentText()
        domicilio_personal = self.obj_form.lne_domicilio_personal.text()
        domi_personal_nro = self.obj_form.lne_numero_domicilio_personal.text()
        localidad_personal = self.obj_form.cbx_localidad_personal.currentText()
        telefono_personal = self.obj_form.lne_telefono_personal.text()
        email_personal2 = self.obj_form.lne_correo_personal.text()
        domicilio_profesional = self.obj_form.lne_domicilio_profesional.text()
        numero_profesional = self.obj_form.lne_numero_profesional.text()
        localidad_profesional = self.obj_form.cbx_localidad_profesional.currentText()
        telefono_profesional = self.obj_form.lne_telefono_profesional.text()
        email_profesional = self.obj_form.lne_email_profesional.text()
        
        obj_N_datos_personales_prof  =N_datos_personales_prof(apellido)
        #obj_N_datos_personales_prof  =N_datos_personales_prof(apellido,nombre,genero,nac,tipo_doc,nro_doc,fec_nac,lugar_nac,estado_civil,domicilio_personal,domi_personal_nro,localidad_personal,telefono_personal,email_personal2,domicilio_profesional,numero_profesional,localidad_profesional,email_profesional)

        
        organismo = self.obj_form.cbx_organismo.currentText()
        funcion = self.obj_form.cbx_funcion.currentText()
        
        if self.obj_form.ckbx_psic_clin_vincular.isChecked():
            psic_clin_vincular =True
           

        if self.obj_form.ckbx_psic_lab_organizacional.isChecked():
            psic_lab_organizacional = True    
        
        if self.obj_form.ckbx_psic_educacional.isChecked():
           psic_educacional = True


        if self.obj_form.ckbx_neuropsic.isChecked():
            neuropsic = True

        if self.obj_form.ckbx_psicoprofilaxis.isChecked():
            psicoprofilaxis =  True
        

        if self.obj_form.ckbx_psiconcologia.isChecked():
            psiconcologia =  True

        if self.obj_form.ckbx_investigacion.isChecked():
            investigacion =  True
        
        if self.obj_form.ckbx_evaluacion_psic.isChecked():
            evaluacion_psic =  True
         
        if self.obj_form.ckbx_psic_forense.isChecked():
            psic_forense =  True
        
        if self.obj_form.ckbx_otros.isChecked():
             otros =  True
         
        nivel_medio = False
        nivel_terciario = False
        nivel_universitario = False

        if self.obj_form.ckbx_docencia.isChecked():
            nivel_medio = str(self.obj_form.ckbx_nivel_medio.isChecked())
            nivel_terciario = self.obj_form.ckbx_nivel_terciario.isChecked()
            nivel_universitario = self.obj_form.ckbx_nivel_universitario.isChecked()
            self.obj_form.resultado.setText(nivel_medio)

        if self.obj_form.ckbx_psic_clin_adultos.isChecked():
            psic_clin_adultos = True

        if self.obj_form.ckbx_psic_clin_nios.isChecked():
            psic_clin_nios = True
        
        if self.obj_form.ckbx_orient_psicoanalitica.isChecked():
            if self.obj_form.ckbx_orient_psicoanalitica.isChecked():
                orient_psicoanalitica = True
            if self.obj_form.ckbx_orient_cognitivo.isChecked():
                orient_cognitivo = True
            if self.obj_form.ckbx_orient_sistemica.isChecked():
                orient_sistemica = True

            if self.obj_form.ckbx_otras_orientaciones.isChecked():
                otras_orientaciones = self.obj_form.lne_otras_orientaciones.text()

        trabaja_obra_social = False
        if self.obj_form.ckbx_si.isChecked():
            trabaja_obra_social = True

        cuit = self.obj_form.lne_cuit.text()
        isnn = self.obj_form.lne_isnn.text()
        if self.obj_form.cbx_dec_jur_si.isChecked():
            dec_jur_si = True

        nro_legajo = self.obj_form.lne_nro_legajo.text()
       
       # obj_N_datos_profesionales = N_datos_profesionales(organismo, funcion ,psic_clin_vincular,psic_lab_organizacional, psic_educacional ,neuropsic ,psicoprofilaxis, psiconcologia , investigacion, evaluacion_psic, psic_forense, otros ,nivel_medio,nivel_terciario , nivel_universitario, psic_clin_adultos, psic_clin_nios, orient_psicoanalitica,  orient_sistemica, orient_cognitivo ,otras_orientaciones, trabaja_obra_social, cuit ,isnn , dec_jur_si, nro_legajo)


        tipo_de_cuenta = self.obj_form.cbx_tipo_de_cuenta.currentText()
        banco = self.obj_form.cbx_banco.currentText()
        nro_cuenta = self.obj_form.lne_nro_cuenta.text()
        cbu = self.obj_form.lne_cbu.text()
        #obj_N_datos_bancarios=N_datos_bancarios(tipo_de_cuenta , banco ,nro_cuenta,cbu)
       # pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        #lista de titulos profesionales aguardar
        obj_N_datos_personales_prof2=N_datos_personales_prof(apellido)
        obj_N_datos_personales_prof2.guardar(self.list_titulos_prof)






       
        #self.listregistros =self.obj_form.tw_registrotitulos

        for item in self.list_titulos_prof: 
            item.universidad
        #for nro in range(self.obj_form.tw_registrotitulos.rowCount()):
         #   result = self.obj_form.tw_registrotitulos.row[nro].column[1]


    def agregar(self):
        titulo_grado = self.obj_form.cbx_titulo_grado.currentText()
        universidad_grado = self.obj_form.cbx_universidad_grado.currentText()
        dte_fecha_titulo_grado = self.obj_form.dte_fecha_titulo_grado.text()
        dte_fecha_aut_min_educ_grado = self.obj_form.dte_fecha_aut_min_educ_grado.text()
        dte_fecha_aut_min_int_grado = self.obj_form.dte_fecha_aut_min_int_grado.text()   
                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        obj_datos_Academicos = N_datos_academicos(universidad_grado,dte_fecha_aut_min_educ_grado,dte_fecha_aut_min_int_grado,dte_fecha_titulo_grado,titulo_grado)

        self.list_titulos_prof.append(obj_datos_Academicos)
        

        #AGREGAR REGISTROS EN LA GRILLA
        rowPosition = self.obj_form.tw_registrotitulos.rowCount()
        self.obj_form.tw_registrotitulos.insertRow(rowPosition)
        self.obj_form.tw_registrotitulos.setItem(rowPosition , 0, QTableWidgetItem(titulo_grado))
        self.obj_form.tw_registrotitulos.setItem(rowPosition , 1, QTableWidgetItem(universidad_grado))
        self.obj_form.tw_registrotitulos.setItem(rowPosition , 2, QTableWidgetItem(str(dte_fecha_titulo_grado)))
        self.obj_form.tw_registrotitulos.setItem(rowPosition , 3, QTableWidgetItem(str(dte_fecha_aut_min_educ_grado)))
        self.obj_form.tw_registrotitulos.setItem(rowPosition , 4, QTableWidgetItem(str(dte_fecha_aut_min_int_grado)))




app = QApplication(sys.argv)
dialogo= Dialogo()
dialogo.show()
app.exec_()