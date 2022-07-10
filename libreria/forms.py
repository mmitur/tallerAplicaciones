from cProfile import label
from secrets import choice
from tkinter import Widget
from django import forms
from .models import Pacientes, Usuario,Atenciones,Medico,Examenes,Medicamentos

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['TipoUsuario']
        widgets = {'TipoUsuario': forms.Select()}


class atencionesForm(forms.ModelForm):
    rutPaciente = forms.ModelChoiceField(queryset=Pacientes.objects.all(),widget=forms.Select(attrs={"class": "form-select"}),label="Rut Paciente")
    rutMedico = forms.ModelChoiceField(queryset=Medico.objects.all(),widget=forms.Select(attrs={"class": "form-select"}),label="Rut Medico")
    diagnostico = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}),label="Diagnostico:")
    anamnesis = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}),label="Anamnesis:")
    fechaAtencion = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control"}),label="Fecha Atencion")
    hora = forms.TimeField(widget=forms.TimeInput(attrs={"class":"form-control"}),label="Hora")
    sala = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    medicamento = forms.ModelMultipleChoiceField(queryset=Medicamentos.objects.all(),widget=forms.CheckboxSelectMultiple(attrs={"class": "check-control"}),label="Medicamentos")
    examenes = forms.ModelMultipleChoiceField(queryset=Examenes.objects.all(),widget=forms.CheckboxSelectMultiple(attrs={"class": "check-control"}),label="Examenes")

    class Meta:
        model = Atenciones
        fields = ['idAtencion','rutPaciente','rutMedico','diagnostico','anamnesis','fechaAtencion',
        'hora','sala','medicamento','examenes']



estado_genero = [(True,'Masculino'),(False,'Femenino')]

class pacienteForm(forms.ModelForm):
    rutPaciente = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),label="Rut del paciente")
    nombrePaciente = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),label="Nombre del paciente")
    apellidoPaciente = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),label="Apellido del paciente")
    fechaNacimiento = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control"}),label="Fecha de nacimiento")
    genero = forms.CharField(widget=forms.RadioSelect(choices=estado_genero),label="Genero")

    class Meta:
        model = Pacientes
        fields = ['rutPaciente','nombrePaciente','apellidoPaciente','fechaNacimiento','genero']