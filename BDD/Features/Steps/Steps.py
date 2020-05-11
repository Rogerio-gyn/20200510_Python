from calc import soma
from behave import step

@step('somar "{val_0:d}" com "{val_1:d}"')
def teste_soma(context, val_0, val_1):
    global result
    result = soma(val_0, val_1)

@step('resultado deve ser "{resultado:d}"')
def teste_soma_resultado(context,resultado):
    assert result == resultado