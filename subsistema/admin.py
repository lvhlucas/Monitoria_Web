from django.contrib import admin

from .models import Curso,Materia,Aluno,EstadoMonitor,RegistroAtendimento,Monitor

admin.site.register(Curso)
admin.site.register(Aluno)
admin.site.register(Materia)
admin.site.register(Monitor)
admin.site.register(EstadoMonitor)
admin.site.register(RegistroAtendimento)
# Register your models here.
