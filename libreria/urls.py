from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='index'),
    path('inicio', views.inicio, name='inicio'),
    path('atenciones',views.atenciones, name='atenciones'),
    path('eliminar/<int:id>',views.eliminar,name="eliminar"),
    path('editar/<int:id>',views.editar,name='editar'),
    path('crearPaciente',views.crearPaciente, name='crearPaciente'),
]

