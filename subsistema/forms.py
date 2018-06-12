from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AlunoPedeMonitor,Aluno,RegistroAtendimento,Curso

class AlunoPedeMonitorForm(forms.ModelForm):
    class Meta:
        model = AlunoPedeMonitor
        fields = ('comentario', 'materia','periodo')

class AlunoCadastraForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    semestreEntrada=forms.CharField(max_length=5)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','semestreEntrada')

class AlunoRegistraAtendimentoForm(forms.ModelForm):        
    class Meta:
        model = RegistroAtendimento
        fields = ('dia', 'horasMinistradas','linkListaPresenca','qtdAlunosPresentes')   
        