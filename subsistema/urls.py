from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'subsistema'
urlpatterns = [           
    path('login/', views.login, name='login'),    
    path('logout/', views.logout, name='logout'),    
    path('login/cadastrar/', views.alunoCadastra, name='alunoCadastra'),       
    path('alunopedemonitor/', views.AlunoPedeMonitor, name='AlunoPedeMonitor'),       
]
