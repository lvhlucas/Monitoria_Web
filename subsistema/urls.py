from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'subsistema'
urlpatterns = [
    #tela inicial, dois botões para aluno ou professor       
    path('login/', views.login, name='login'),    
    path('login/cadastrar/', views.alunoCadastra, name='alunoCadastra'),       
    path('alunopedemonitor/', views.AlunoPedeMonitor, name='AlunoPedeMonitor'),       
]
