from django.shortcuts import  render
from .models import Aluno,Curso,Materia
from .forms import AlunoCadastraForm,AlunoPedeMonitorForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
 
 
def alunoCadastra(request): 
    if request.method == "POST":
        form = AlunoCadastraForm(request.POST)         
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal            
            user.save()
            raw_password = form.cleaned_data.get('password1')            
            return render(request,'subsistema/alunoHome.html')
    else:
        form = AlunoCadastraForm()
    return render(request,'subsistema/alunoCadastra.html',{'curso':Curso.objects.all(),'User':User.objects.all()})
 
@login_required(login_url='/login/')
def alunoHome(request):
    return render(request,'subsistema/alunoHome.html')
    
@login_required(login_url='/login/')
def AlunoPedeMonitor(request):
    if request.method == "POST":
        form = AlunoPedeMonitorForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            return render(request,'subsistema/alunoHome.html')
    else:
        form = AlunoPedeMonitorForm()
    return render(request, 'subsistema/AlunoPedeMonitor.html', {'form': form})

