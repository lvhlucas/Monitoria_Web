from behave import given, when, then
from test.factories.user import UserFactory, AlunoGroupFactory, user_password, MateriaFactory, CursoFactory
from selenium.webdriver.support.ui import Select
from subsistema.models import Materia

@given(u'Usuario é autenticado')
def step_impl(context):
    UserFactory.create(groups=(AlunoGroupFactory.create(),))
    br = context.browser
    br.get(context.base_url+'/login/')
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    br.find_element_by_name('username').send_keys('foo')
    br.find_element_by_name('password').send_keys(user_password)
    br.find_element_by_name('submit').click()



@given(u'O aluno informa os seguintes campos: "<comentario>", "<prog1>", "<semestre>"')
def step_impl(context):
    MateriaFactory()
    br = context.browser
    br.get(context.base_url + '/subsistema/alunopedemonitor/')
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    select = Select(br.find_element_by_id('id_materia'))
    select.select_by_visible_text('prog1')
    br.find_element_by_name('comentario').send_keys('comentarioTeste')
    br.find_element_by_name('periodo').send_keys('2000')


@when(u'O aluno submeter o formulario')
def step_impl(context):
    context.browser.find_element_by_name('submit').click()


@then(u'Ele é redirecionado para a home page')
def step_impl(context):
    assert context.browser.current_url.endswith('/home/')

