from django import forms

from .models import AlunoPedeMonitor

class AlunoPedeMonitorForm(forms.ModelForm):

    class Meta:
        model = AlunoPedeMonitor
        fields = ('comentario', 'materia')
