from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from .models import Aluno,Curso,Materia
from django.contrib.auth.decorators import login_required



def alunoCadastra(request): 
    if request.method == "POST":                
        aluno=Aluno(nomePessoa=request.POST['nome'],email=request.POST['email'],semestreEntrada=request.POST['semestre'],curso=Curso.objects.get(pk=request.POST['UmCurso']))
        aluno.save()
        messages.info(request, 'Conta criada com sucesso!')
        return HttpResponseRedirect(reverse('subsistema:alunoLogin'))
    return render(request,'subsistema/alunoCadastra.html',{'curso':Curso.objects.all(),'aluno':Aluno.objects.all()})
  
#@login_required
def AlunoPedeMonitor(request);
    if request.method == "POST":
        form = AlunoPedeMonitorForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.comentario = request.cometario
            pedido.materia = request.materia
            pedido.save()
            return redirect('')
    else:
        form = PostForm()
    return render(request, 'subsistema/AlunoPedeMonitor.html', {'form': form})

