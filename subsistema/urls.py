from django.urls import path
from . import views

app_name = 'subsistema'
urlpatterns = [                  
    path('cadastrar/', views.aluno_cadastra, name='aluno_cadastra'),
    path('alunopedemonitor/', views.aluno_pede_monitor, name='aluno_pede_monitor'),
    path('home/', views.aluno_home, name='aluno_home'),
    path('registroatendimento/', views.aluno_registra_atendimento, name='aluno_registra_atendimento'),
    path('inscrever/', views.aluno_inscreve, name='aluno_inscreve'),
    path('falha/', views.falha, name='falha_'),
]
