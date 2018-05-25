from django.contrib import admin

from .models import Curso,Materia,Aluno,EstadoMonitor,RegistroAtendimento,Monitor,AlunoPedeMonitor

admin.site.register(Curso)
admin.site.register(Aluno)
admin.site.register(Materia)
admin.site.register(Monitor)
admin.site.register(EstadoMonitor)
admin.site.register(AlunoPedeMonitor)
admin.site.register(RegistroAtendimento)
# Register your models here.
