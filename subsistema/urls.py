from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'subsistema'
urlpatterns = [                  
    path('cadastrar/', views.alunoCadastra, name='alunoCadastra'),       
    path('alunopedemonitor/', views.AlunoPedeMonitor, name='AlunoPedeMonitor'),       
]
