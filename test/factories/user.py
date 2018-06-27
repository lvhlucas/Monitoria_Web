import factory
import django.contrib.auth.models as auth_models
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password
from subsistema.models import Materia, Curso, Aluno

user_password = 'foo'


class AlunoGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = auth_models.Group

    name = 'aluno'


class MonitorGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = auth_models.Group

    name = 'monitor'


class CursoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Curso

    nomeCurso = "bsi"


class MateriaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Materia
    nomeMateria = 'prog1'
    curso = factory.SubFactory(CursoFactory)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = auth_models.User

    first_name = "first_name_test"
    last_name = "last_name_test"
    username = "foo"
    password = make_password(user_password)
    email = "foo@exemple.com"
    is_active = True

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for group in extracted:
                self.groups.add(group)
