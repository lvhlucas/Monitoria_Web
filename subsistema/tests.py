from django.test import TestCase
from django.urls import resolve
from subsistema.views import AlunoPedeMonitor
from django.template.loader import render_to_string
from django.contrib.auth.models import User,Group
from .forms import AlunoCadastraForm,AlunoRegistraAtendimentoForm,AlunoPedeMonitorForm


class AlunoPedeMonitorTest(TestCase):
    #test_user1 = User.objects.create_user(username='testuser1', password='12345')
    #test_user1.save()
    #my_group = Group.objects.get(name='aluno') 
    #my_group.user_set.add(test_user1)

    def test_AlunoPedeMonitor_returns_correct_html(self):
        self.client.login(username='testuser1', password='12345')
        response = self.client.get('/subsistema/alunopedemonitor/')  
        self.assertTemplateUsed(response, 'subsistema/AlunoPedeMonitor.html') 
  
    def test_form_validation_for_blank_items(self):
        form = AlunoPedeMonitorForm(data={'comentario':'1234', 'materia':None,'periodo':''})
        self.assertFalse(form.is_valid())