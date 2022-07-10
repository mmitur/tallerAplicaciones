from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Atenciones, Usuario
# Create your views here.
from .forms import UsuarioForm, atencionesForm,pacienteForm

def inicio(request):
    inicio = Atenciones.objects.all()
    return render(request,'paginas/inicio.html',{'inicio':inicio})

def index(request):
    return render(request)

def atenciones(request):
    form = atencionesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('inicio')
    return render(request, 'paginas/atenciones.html', {'form': form})

def editar(request,id):
    atencion = Atenciones.objects.get(idAtencion=id)
    form = atencionesForm(request.POST or None, request.FILES or None, instance=atencion)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('inicio')
    return render(request,'paginas/editar.html',{'form': form})

def eliminar(request,id):
    eliminar = Atenciones.objects.get(idAtencion=id)
    eliminar.delete()
    return redirect('inicio')

def crearPaciente(request):
    form = pacienteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('inicio')
    return render(request, 'paginas/crearPaciente.html',{'form' : form})
