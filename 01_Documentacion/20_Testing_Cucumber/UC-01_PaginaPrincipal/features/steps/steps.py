from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = 'https://pagina-testing-dusky.vercel.app/'

def capture_screenshot(context, name):
    screenshot_path = f'screenshots/{name}.png'
    context.browser.save_screenshot(screenshot_path)
    return screenshot_path

@given('el usuario accede a la página principal de IMPACTONET')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get(BASE_URL)
    context.browser.maximize_window()
    context.screenshot_path = capture_screenshot(context, 'pagina_principal')
    time.sleep(2)

# Escenario 1: Navegar a una URL incorrecta
@when('el usuario intenta acceder a una página no existente')
def step_impl(context):
    context.browser.get(BASE_URL + 'pagina_no_existente')
    time.sleep(2)

@then('el sistema muestra un error 404')
def step_impl(context):
    assert "404" in context.browser.page_source, "No se mostró el error 404"
    context.screenshot_path = capture_screenshot(context, 'error_404')

# Escenario 2: Click en un enlace incorrecto
@when('el usuario hace clic en un enlace incorrecto')
def step_impl(context):
    try:
        context.browser.find_element(By.LINK_TEXT, 'Planes').click()
        time.sleep(2)
    except:
        pass  # Ignorar el error para forzar un fallo en el siguiente paso

@then('el sistema redirige a una página de error')
def step_impl(context):
    # Forzamos el fallo asegurando que no se redirige a la página de planes correcta
    assert "Planes" not in context.browser.page_source, "No se redirigió a una página de error"
    context.screenshot_path = capture_screenshot(context, 'error_redireccion')

# Escenario 3: Navegación fallida por la página principal
@when('el usuario navega por la página principal correctamente')
def step_impl(context):
    try:
        context.browser.find_element(By.LINK_TEXT, 'Inicio').click()
        time.sleep(2)
    except:
        pass  # Ignorar el error para forzar un fallo en el siguiente paso

@then('el sistema muestra la página principal correctamente')
def step_impl(context):
    # Forzamos el fallo asegurando que el texto clave no se encuentra en la página principal
    assert "Bienvenido a IMPACTONET" not in context.browser.page_source, "La página principal se mostró correctamente"
    context.screenshot_path = capture_screenshot(context, 'pagina_principal_incorrecta')

@then('el sistema muestra los beneficios correctamente')
def step_impl(context):
    # Forzamos el fallo asegurando que los beneficios no se muestran correctamente
    try:
        benefits = context.browser.find_element(By.CLASS_NAME, 'benefits-grid')
        assert not benefits.is_displayed(), "Se mostraron los beneficios correctamente"
    except:
        pass  # Ignorar el error para forzar un fallo
    context.screenshot_path = capture_screenshot(context, 'beneficios_incorrectos')

# Escenario 4: Click en un enlace roto
@when('el usuario hace clic en un enlace roto')
def step_impl(context):
    try:
        context.browser.find_element(By.LINK_TEXT, 'Acerca de Nosotros').click()
        time.sleep(2)
    except:
        pass  # Ignorar el error para forzar un fallo en el siguiente paso

@then('el sistema muestra una página de error')
def step_impl(context):
    # Forzamos el fallo asegurando que no se muestra la página correcta
    assert "Acerca de Nosotros" not in context.browser.page_source, "No se mostró una página de error"
    context.screenshot_path = capture_screenshot(context, 'error_pagina_rota')

# Escenario 5: Cargar un recurso inexistente
@when('el usuario intenta cargar un recurso inexistente')
def step_impl(context):
    context.browser.get(BASE_URL + 'recurso_no_existente.png')
    time.sleep(2)

@then('el sistema muestra un mensaje de error de recurso no encontrado')
def step_impl(context):
    assert "Recurso no encontrado" in context.browser.page_source or "404" in context.browser.page_source, "No se mostró el mensaje de error de recurso no encontrado"
    context.screenshot_path = capture_screenshot(context, 'error_recurso_no_encontrado')
