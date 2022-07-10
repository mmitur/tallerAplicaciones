from django.contrib import admin
from .models import Usuario,Administrador,Medico,Especialidades,Pacientes,Atenciones,Medicamentos,Examenes

admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Medico)
admin.site.register(Especialidades)
admin.site.register(Pacientes)
admin.site.register(Atenciones)
admin.site.register(Medicamentos)
admin.site.register(Examenes)
# Register your models here.
