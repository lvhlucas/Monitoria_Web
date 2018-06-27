import factory
from django.contrib.auth.models import Group

class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username', 'email')

    # Defaults (can be overrided)
    username = 'foo'
    email = 'foo@example.com'
    password = 'bar'