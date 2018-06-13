from django.db import models
from django.contrib.auth.models import User


class Curso(models.Model):
    nomeCurso = models.CharField(max_length=50)

    def __str__(self):
        return self.nomeCurso


class Materia(models.Model):    
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nomeMateria = models.CharField(max_length=50)

    def __str__(self):
        return self.nomeMateria


class Aluno(models.Model):
    semestreEntrada = models.CharField(max_length=5)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Aluno:'+self.user.first_name+' '+self.user.last_name


class AlunoPedeMonitor(models.Model):
    comentario = models.TextField()
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=5)

    def __str__(self):
        return "Pedido:"+self.materia.nomeMateria


class EstadoMonitor(models.Model):
    nomeEstado = models.CharField(max_length=9)

    def __str__(self):
        return self.nomeEstado


class RegistroAtendimento(models.Model):
    dia = models.DateTimeField('date published')
    horasMinistradas = models.IntegerField(default=0)
    linkListaPresenca = models.CharField(max_length=200)
    qtdAlunosPresentes = models.IntegerField(default=0)
    responsavel = models.ForeignKey(Aluno, on_delete=models.CASCADE)


class Monitor(models.Model):
    horarioAtendimento = models.CharField(max_length=200)
    estado = models.ForeignKey(EstadoMonitor, on_delete=models.CASCADE)        
    atendimentos = models.ForeignKey(RegistroAtendimento, on_delete=models.CASCADE)
