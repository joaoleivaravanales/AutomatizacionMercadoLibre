from pytest_bdd import scenario, given, when, then, parsers
import pytest
from pages.validar_textos_iphone import ValidarTextosIphonePage


@scenario("../features/validar_iphone.feature", "Buscar iphone en MercadoLibre")
def test_validar_textos_iphone():
    pass


@pytest.fixture
def validar_textos_iphone_page(page):
    return ValidarTextosIphonePage(page)


@given("el usuario está en la pagina principal")
def abrir_pagina_principal(validar_textos_iphone_page):
    validar_textos_iphone_page.abrir_pagina_principal()


@when(parsers.parse('busca el producto "{producto}"'))
def buscar_producto(validar_textos_iphone_page, producto):
    validar_textos_iphone_page.buscar_producto(producto)

@when("Presiono en el primer resultado")
def presionar_primer_resultado(validar_textos_iphone_page):
    validar_textos_iphone_page.presionar_primer_resultado()


@then(parsers.parse('Verifico que el titulo del producto sea "{titulo}"'))
def verificar_titulo_producto(validar_textos_iphone_page, titulo):
    validar_textos_iphone_page.verificar_titulo_producto(titulo)
