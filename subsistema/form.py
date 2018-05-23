from django import forms

from .models import PedidoMonitor

class PedidoMonitorForm(forms.ModelForm):

    class Meta:
        model = PedidoMonitor
        fields = ('comentario', 'materia')