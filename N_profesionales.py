import sys
import datetime 
from E_datos_academicos import E_datos_academicos
from PyQt5.QtCore import pyqtRemoveInputHook


class N_datos_bancarios(object):
    tipo_de_cuenta = "" 
    banco = ""
    nro_cuenta = ""
    cbu= ""

    def __int__(self,tipo_de_cuenta , banco ,nro_cuenta,cbu):
        self.tipo_de_cuenta = tipo_de_cuenta
        self.banco= banco
        self.nro_cuenta= nro_cuenta
        self.cbu = cbu

class N_datos_personales_prof(object):
    """docstring for ClassName"""
    apellido = ""
    nombre = ""
    genero = ""
    nac = ""
    tipo_doc = ""
    nro_doc =""
    fec_nac = datetime
    lugar_nac =  datetime
    estado_civil =False
    domicilio_personal = ""
    domi_personal_nro = ""
    localidad_personal = ""
    telefono_personal = ""
    email_personal = ""
    domicilio_profesional = ""
    numero_profesional = ""
    localidad_profesional = ""
    telefono_profesional = ""
    email_profesional = ""

    def __init__(self,apellido):
        self.apellido=apellido
    #def __init__(self,apellido,nombre,genero,nac,tipo_doc,nro_doc,fec_nac,lugar_nac,estado_civil,domicilio_personal,domi_personal_nro,localidad_personal,telefono_personal,email_personal,domicilio_profesional,numero_profesional,localidad_profesional,telefono_profesional,email_profesional):
       # self.apellido = apellido
        #self.nombre = nombre
       # self.genero = genero
       # self.nac = nac
       # self.tipo_doc = tipo_doc
       # self.nro_doc = nro_doc
        #self.fec_nac = fec_nac
        #self.lugar_nac = lugar_nac
        #self.estado_civil = estado_civil
        #self.domicilio_personal =domicilio_personal
        #self.domi_personal_nro = domi_personal_nro
        #self.localidad_personal = localidad_personal
        #self.telefono_personal = telefono_personal
        #self.email_personal = email_personal
        #self.domicilio_profesional = domicilio_profesional
        #self.numero_profesional = numero_profesional
        #self.localidad_profesional = localidad_profesional
        #self.telefono_profesional = telefono_profesional
        #self.email_profesional = email_profesional

  #  def guardar( N_datos_generales,N_profesionales, N_datos_academicos ,N_datos_bancarios):
                #pyqtRemoveInputHook()
   #     import pdb; pdb.set_trace()
    #    obj_E_datos_academicos= E_datos_academicos(1,1)
     #   obj_E_datos_academicos.(N_datos_academicos)

    def guardar(self, list_N_datos_academicos ):
#        pyqtRemoveInputHook()
 #       import pdb; pdb.set_trace()
        obj_E_datos_academicos= E_datos_academicos(1,1)
        obj_E_datos_academicos.guardar(list_N_datos_academicos)


class N_datos_profesionales(object):
    organismo=""
    funcion=""
    psic_clin_vincular=False
    psic_lab_organizacional=False
    psic_educacional =False
    neuropsic = False
    psicoprofilaxis =False
    psiconcologia=False
    investigacion =False
    evaluacion_psic=False
    psic_forense =False
    otros =""
    nivel_medio =False
    nivel_terciario =False
    nivel_universitario =False
    psic_clin_adultos=False
    psic_clin_nios =False
    orient_psicoanalitica=False
    orient_sistemica=False
    orient_cognitivo=False
    otras_orientaciones=False
    trabaja_obra_social=False
    cuit = ""
    isnn = ""
    dec_jur_si =False
    nro_legajo = ""

    def __init__(self, organismo, funcion ,psic_clin_vincular,psic_lab_organizacional, psic_educacional ,neuropsic ,psicoprofilaxis, psiconcologia , investigacion, evaluacion_psic, psic_forense, otros ,nivel_medio,nivel_terciario , nivel_universitario, psic_clin_adultos, psic_clin_nios, orient_psicoanalitica,  orient_sistemica, orient_cognitivo ,otras_orientaciones, trabaja_obra_social, cuit ,isnn , dec_jur_si, nro_legajo):
        self.organismo= organismo
        self.funcion=funcion
        self.psic_clin_vincular= psic_clin_vincular
        self.psic_lab_organizacional= psic_lab_organizacional
        self.psic_educacional =psic_educacional
        self.neuropsic = neuropsic
        self.psicoprofilaxis =psicoprofilaxis
        self.psiconcologia=psiconcologia
        self.investigacion =investigacion
        self.evaluacion_psic=evaluacion_psic
        self.psic_forense =psic_forense
        self.otros = otros
        self.nivel_medio = nivel_medio
        self.nivel_terciario = nivel_terciario
        self.nivel_universitario = nivel_universitario
        self.psic_clin_adultos = psic_clin_adultos
        self.psic_clin_nios = psic_clin_nios
        self.orient_psicoanalitica = orient_psicoanalitica
        self.orient_sistemica = orient_sistemica
        self.orient_cognitivo = orient_cognitivo
        self.otras_orientaciones=otras_orientaciones
        self.trabaja_obra_social=trabaja_obra_social
        self.cuit = cuit
        self.isnn = isnn
        self.dec_jur_si =dec_jur_si
        self.nro_legajo = nro_legajo

class N_datos_academicos(object):
    import datetime 
    universidad=""
    fecha_titulo=datetime 
    fecha_min=datetime
    fecha_mej=datetime
    titulo= ""

    def __init__(self, universidad,fecha_mej,fecha_min,fecha_titulo,titulo):
        self.universidad=universidad
        self.fecha_titulo=fecha_titulo
        self.fecha_min=fecha_min
        self.fecha_mej=fecha_mej
        self.titulo= titulo
