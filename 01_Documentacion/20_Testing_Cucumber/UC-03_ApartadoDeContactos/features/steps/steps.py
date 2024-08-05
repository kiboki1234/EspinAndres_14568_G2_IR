from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = 'https://pagina-testing-dusky.vercel.app/'

def capture_screenshot(context, name):
    screenshot_path = f'screenshots/{name}.png'
    context.browser.save_screenshot(screenshot_path)
    return screenshot_path

@given('el usuario accede a la página de IMPACTONET')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get(BASE_URL)
    context.browser.maximize_window()
    context.screenshot_path = capture_screenshot(context, 'Ingreso a contactos')
    time.sleep(2)
    

@when('el usuario se dirige al apartado de contacto')
def step_impl(context):
    context.browser.find_element(By.LINK_TEXT, 'Contactos').click()
    time.sleep(2)


@then('el sistema despliega el formulario de contacto')
def step_impl(context):
    assert context.browser.find_element(By.ID, 'contact-form').is_displayed(), "No se encontró el formulario de contacto"
    context.screenshot_path = capture_screenshot(context, 'formulario_contacto')

@when('el usuario llena el formulario con "{name}", "{email}" y "{message}"')
def step_impl(context, name, email, message):
    context.browser.find_element(By.ID, 'name').send_keys(name)
    context.browser.find_element(By.ID, 'email').send_keys(email)
    context.browser.find_element(By.ID, 'message').send_keys(message)
    context.screenshot_path = capture_screenshot(context, 'llenar_formulario')

@when('el usuario presiona el botón "Enviar"')
def step_impl(context):
    context.browser.find_element(By.ID, 'submit-button').click()
    time.sleep(2)
    context.screenshot_path = capture_screenshot(context, 'enviar_formulario')

@then('el sistema envía la información del formulario al correo de la empresa')
def step_impl(context):
    # Aquí podrías agregar una verificación adicional si tienes una forma de comprobar el envío del correo
    assert "Mensaje enviado" in context.browser.page_source, "El mensaje no se envió correctamente"
    context.screenshot_path = capture_screenshot(context, 'mensaje_enviado')

@then('el usuario ve un mensaje de confirmación de envío exitoso')
def step_impl(context):
    assert "Mensaje enviado" in context.browser.page_source, "El usuario no vio el mensaje de confirmación de envío"
    context.screenshot_path = capture_screenshot(context, 'confirmacion_envio')

@then('el sistema muestra un mensaje de error solicitando llenar todos los campos')
def step_impl(context):
    assert "Por favor, complete todos los campos" in context.browser.page_source, "No se mostró el mensaje de error"
    context.screenshot_path = capture_screenshot(context, 'error_campos_vacios')

@then('el sistema muestra la dirección física "{direccion}"')
def step_impl(context, direccion):
    assert direccion in context.browser.page_source, f"No se mostró la dirección física {direccion}"
    context.screenshot_path = capture_screenshot(context, 'direccion_fisica')

@then('el sistema muestra el número telefónico "{telefono}"')
def step_impl(context, telefono):
    assert telefono in context.browser.page_source, f"No se mostró el número telefónico {telefono}"
    context.screenshot_path = capture_screenshot(context, 'numero_telefonico')

@then('el sistema muestra el correo electrónico "{correo}"')
def step_impl(context, correo):
    assert correo in context.browser.page_source, f"No se mostró el correo electrónico {correo}"
    context.screenshot_path = capture_screenshot(context, 'correo_electronico')

@then('el sistema muestra un mapa interactivo con la ubicación de la empresa')
def step_impl(context):
    # Aquí deberías agregar un ID o clase al mapa interactivo en el HTML para localizarlo
    # Por ejemplo: <div id="google-map"></div>
    assert context.browser.find_element(By.ID, 'google-map').is_displayed(), "No se mostró el mapa interactivo"
    context.screenshot_path = capture_screenshot(context, 'mapa_interactivo')
