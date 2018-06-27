from behave import given, when
from test.factories.user import UserFactory, user_password, MonitorGroupFactory


@given(u'Usuario é autenticado e é um monitor')
def step_impl(context):
    UserFactory.create(groups=(MonitorGroupFactory.create(),))
    br = context.browser
    br.get(context.base_url+'/login/')
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    br.find_element_by_name('username').send_keys('foo')
    br.find_element_by_name('password').send_keys(user_password)
    br.find_element_by_name('submit').click()



@given(u'O monitor informa os seguintes campos: 2018-12-31, 2, linkimg.png, qtdaluno')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/subsistema/registroatendimento/')
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_name('dia').send_keys('2018-12-31')
    br.find_element_by_name('horasMinistradas').send_keys('2')
    br.find_element_by_name('linkListaPresenca').send_keys('linkimg.png')
    br.find_element_by_name('qtdAlunosPresentes').send_keys('20')


@when(u'O monitor submeter o formulario')
def step_impl(context):
    context.browser.find_element_by_name('submit').click()
    print('stp2', context.browser.current_url)



