from django.shortcuts import render
from .forms import AlunoCadastraForm, AlunoRegistraAtendimentoForm, AlunoPedeMonitorForm, AlunoInscreveVagaForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from .models import Curso, RegistroAtendimento, Aluno
from django.urls import reverse
from django.http import HttpResponseRedirect


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


def aluno_cadastra(request):
    if request.method == "POST":
        form = AlunoCadastraForm(request.POST)         
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() 
            user.save()
            my_group = Group.objects.get(name='aluno') 
            my_group.user_set.add(user)
            Aluno(semestreEntrada=form.cleaned_data['semestreEntrada'], curso=form.cleaned_data['curso'],
                  user=user).save()
            return HttpResponseRedirect(reverse('subsistema:aluno_home'))
    else:
        form = AlunoCadastraForm()
    return render(request, 'subsistema/alunoCadastra.html', {'curso': Curso.objects.all(), 'form': form})


@user_passes_test(aluno_logado, login_url='/login/')
def aluno_home(request):
    return render(request, 'subsistema/alunoHome.html')


@user_passes_test(aluno_logado, login_url='/login/')
def aluno_pede_monitor(request):
    if request.method == "POST":
        form = AlunoPedeMonitorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('subsistema:aluno_home'))
        else:
            return HttpResponseRedirect(reverse('subsistema:falha_'))
    else:
        form = AlunoPedeMonitorForm()
    return render(request, 'subsistema/AlunoPedeMonitor.html', {'form': form})


@user_passes_test(monitor_logado, login_url='/login/')
def aluno_registra_atendimento(request):
    if request.method == "POST":
        form = AlunoRegistraAtendimentoForm(request.POST)
        if form.is_valid():
            dia = form.cleaned_data['dia']
            horas_ministradas = form.cleaned_data['horasMinistradas']
            link_lista_presenca = form.cleaned_data['linkListaPresenca']
            qtd_alunos_presentes = form.cleaned_data['qtdAlunosPresentes']
            RegistroAtendimento(dia=dia, horasMinistradas=horas_ministradas, linkListaPresenca=link_lista_presenca
                                , qtdAlunosPresentes=qtd_alunos_presentes, responsavel=request.user).save()

            return HttpResponseRedirect(reverse('subsistema:aluno_home'))
    else:
        form = AlunoRegistraAtendimentoForm()

    return render(request, 'subsistema/alunoRegistraAtendimento.html', {'form': form})


@user_passes_test(aluno_logado, login_url='/login/')    
def aluno_inscreve(request):
    if request.method == "POST":
        form = AlunoInscreveVagaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('subsistema:aluno_home'))
    else:
        form = AlunoInscreveVagaForm()

    return render(request, 'subsistema/alunoInscreve.html', {'form': form})


def falha(request):
    return render(request, 'subsistema/falha.html')