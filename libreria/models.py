from gc import DEBUG_COLLECTABLE
from pyexpat import model
from tabnanny import verbose
from time import timezone
from xml.sax.xmlreader import AttributesImpl
from django.db import models
from datetime import datetime,date


# Create your models here.

estado_usuario = [(True,'Medico'),(False,'Administrador')]

estado_genero = [(True,'Masculino'),(False,'Femenino')]

class Usuario(models.Model):
    id= models.AutoField(primary_key=True)
    TipoUsuario = models.BooleanField(verbose_name='Tipo de Usuario',choices=estado_usuario,default=True)

    def __str__(self):
        user = ""
        if self.TipoUsuario==False:
            user = "Administrador"
        else:
            user = "Medico"

        fila = "Usuario: " + str(self.id) + " - " + "Tipo de usuario: " + user
        return fila


class Administrador(models.Model):
    rut=models.CharField(primary_key=True,default=1,max_length=9)
    idUsuario=models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)
    nombre= models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    nombreUsuario = models.CharField(max_length=10)
    contrasenaUsuario = models.CharField(max_length=10)
    fechaNacimiento = models.DateField(verbose_name='Fecha de Nacimiento',auto_now_add=False,auto_now=False,blank=True)
    genero = models.BooleanField(verbose_name='Genero', choices=estado_genero)

    def __str__(self):
        return self.rut

    class Meta:
        verbose_name= "Administrador_1"
        db_table= 'Administrador'




class Especialidades(models.Model):
    codigoEspecialidad = models.AutoField(primary_key=True)
    nombre_Especialidad = models.CharField(max_length=15)

    def __str__(self):
       return self.nombre_Especialidad
    
    class Meta:
        verbose_name = "Especialidades_1"
        db_table = "especialidadess"

class Medico(models.Model):
    rut=models.CharField(primary_key=True,default=1,max_length=9)
    idUsuario=models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)
    nombre= models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    nombreUsuario = models.CharField(max_length=10)
    contrasenaUsuario = models.CharField(max_length=10)
    fechaNacimiento = models.DateField(verbose_name='Fecha de Nacimiento',auto_now_add=False,auto_now=False,blank=True)
    genero = models.BooleanField(verbose_name='Genero', choices=estado_genero)
    especialidadess = models.ManyToManyField(Especialidades)

    def __str__(self):
        return self.nombre + " " + self.apellido + " " + self.rut

    class Meta:
        verbose_name= "Medico_1"
        db_table= 'Medico'  


class Pacientes(models.Model):
    rutPaciente = models.CharField(max_length=9,primary_key=True)
    nombrePaciente = models.CharField(max_length=15)
    apellidoPaciente = models.CharField(max_length=15)
    fechaNacimiento = models.DateField(auto_now_add=False,auto_now=False,blank=True)
    genero = models.BooleanField(choices=estado_genero,verbose_name='Genero')

    def __str__(self):
        fila= ""
        fila = self.nombrePaciente + " " + self.apellidoPaciente + " - " + self.rutPaciente
        return fila

    class Meta:
        verbose_name= "Paciente_1"
        db_table = "Paciente__1"



class Examenes(models.Model):
    idExamen = models.AutoField(primary_key=True)
    nombreExamen = models.CharField(max_length=25)
    cantidad = models.IntegerField()

    def __str__(self):
        fila= ""
        fila = "ID Examen: " + str(self.idExamen) + " - Nombre examen: " + self.nombreExamen
        return fila


class Medicamentos(models.Model):
    idMedicamento = models.AutoField(primary_key=True)
    nombreMedicamento = models.CharField(max_length=25)
    cantidad = models.IntegerField()
    
    def __str__(self):
        fila= ""
        fila = "ID Medicamento: " + str(self.idMedicamento) + " - Nombre Medicamento: " + self.nombreMedicamento
        return fila


class Atenciones(models.Model):
    idAtencion = models.AutoField(primary_key=True)
    rutPaciente = models.ForeignKey(Pacientes,null=True,blank=True,on_delete=models.PROTECT)
    rutMedico = models.ForeignKey(Medico,null=True,blank=True,on_delete=models.PROTECT)
    diagnostico = models.TextField(max_length=200)
    anamnesis = models.TextField(max_length=200,blank=True)
    fechaAtencion = models.DateField(auto_now_add=False,auto_now=False,blank=True)
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    sala = models.CharField(max_length=25)
    medicamento = models.ManyToManyField(Medicamentos)
    examenes = models.ManyToManyField(Examenes)

    def __str__(self):
        fila= ""
        fila = "Atencion: " + str(self.idAtencion) + " - Fecha: " + str(self.fechaAtencion) + " - " + str(self.hora)
        return fila





