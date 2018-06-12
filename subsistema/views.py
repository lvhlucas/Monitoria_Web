from django.shortcuts import  render
from .forms import AlunoCadastraForm,AlunoRegistraAtendimentoForm,AlunoPedeMonitorForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User,Group
from .models import Curso

def is_authenticated(user):
    return user.is_authenticated    
def is_aluno(user):    
    return user.groups.filter(name='aluno').exists()   
def is_monitor(user):
    return user.groups.filter(name='monitor').exists()    
def aluno_logado(user):
    return is_authenticated(user) and is_aluno(user)   
def monitor_logado(user):
    return is_authenticated(user) and is_monitor(user)

def alunoCadastra(request):    
    if request.method == "POST":
        form = AlunoCadastraForm(request.POST)         
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() 
            user.save()
            my_group = Group.objects.get(name='aluno') 
            my_group.user_set.add(user)
            return render(request,'subsistema/alunoHome.html')
    else:
        form = AlunoCadastraForm()
    return render(request,'subsistema/alunoCadastra.html',{'curso':Curso.objects.all(),'form':form})
 
@user_passes_test(aluno_logado, login_url='/login/')
def alunoHome(request):
    return render(request,'subsistema/alunoHome.html')
    
@user_passes_test(aluno_logado, login_url='/login/') 
def AlunoPedeMonitor(request):
    if request.method == "POST":
        form = AlunoPedeMonitorForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            return render(request,'subsistema/alunoHome.html')
    else:
        form = AlunoPedeMonitorForm()
    return render(request, 'subsistema/AlunoPedeMonitor.html', {'form': form})
 
@user_passes_test(monitor_logado, login_url='/login/') 
def alunoRegistraAtendimento(request):    
    if request.method == "POST":
        form = AlunoRegistraAtendimentoForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            return render(request,'subsistema/alunoHome.html')
    else:
        form = AlunoRegistraAtendimentoForm()

    return render(request,'subsistema/alunoRegistraAtendimento.html',{'form': form})

@user_passes_test(aluno_logado, login_url='/login/')    
def alunoInscreve(request): 
    #criar vaga de monitoria para exibir
    #buscar no banco
    #if !(datatermino>dataAtual>datainicio) disable button
    
    if request.method == "POST":
        form = AlunoRegistraAtendimentoForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            return render(request,'subsistema/alunoHome.html')
    else:
        form = AlunoRegistraAtendimentoForm()

    return render(request,'subsistema/alunoInscreve.html',{'form': form})
