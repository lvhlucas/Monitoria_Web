from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AlunoPedeMonitor, RegistroAtendimento, VagaMonitor


class AlunoPedeMonitorForm(forms.ModelForm):
    class Meta:
        model = AlunoPedeMonitor
        fields = ('comentario', 'materia', 'periodo')


class AlunoCadastraForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='Inform a name.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    semestreEntrada = forms.CharField(max_length=5)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'semestreEntrada')


class AlunoRegistraAtendimentoForm(forms.ModelForm):
    dia = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = RegistroAtendimento
        fields = ('dia', 'horasMinistradas', 'linkListaPresenca', 'qtdAlunosPresentes')


class AlunoInscreveVagaForm(forms.ModelForm):
    class Meta:
        model = VagaMonitor
        fields = ('qtdInscritos', 'materias', 'professor')