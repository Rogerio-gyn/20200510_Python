from behave import given, when, then

@given(u'que acesso a pagina do Google')
def step_impl(context):
    context.web.get("https://www.google.com.br")


@when(u'realizo uma pesquisa')
def step_impl(context):
    context.element = context.web.find_element_by_name("q")
    context.element.click()
    context.element.send_keys("Pyjamas conf")
    context.element.submit()


@when(u'pesquisa é realizada')
def step_impl(context):
    pass


@then(u'o título da página deve ser validado')
def step_impl(context):
    pass