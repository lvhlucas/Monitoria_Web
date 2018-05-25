from django import forms

from .models import AlunoPedeMonitor,Aluno

class AlunoPedeMonitorForm(forms.ModelForm):

    class Meta:
        model = AlunoPedeMonitor
        fields = ('comentario', 'materia')
        
class AlunoCadastraForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = ('semestreEntrada', 'curso')
        
