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

@when('el usuario presiona el botón "Enviar por WhatsApp"')
def step_impl(context):
    context.browser.find_element(By.ID, 'whatsapp-button').click()  # Asegúrate que este sea el ID correcto
    time.sleep(2)
    context.screenshot_path = capture_screenshot(context, 'enviar_formulario_whatsapp')

@then('el sistema envía la información del formulario al correo de la empresa')
def step_impl(context):
    assert "Mensaje enviado" in context.browser.page_source, "El mensaje no se envió correctamente"
    context.screenshot_path = capture_screenshot(context, 'mensaje_enviado')

@then('el sistema envía la información del formulario por WhatsApp')
def step_impl(context):
    # Verificación adicional si tienes forma de comprobar el envío por WhatsApp
    assert "WhatsApp" in context.browser.page_source, "El mensaje no se envió correctamente por WhatsApp"
    context.screenshot_path = capture_screenshot(context, 'mensaje_enviado_whatsapp')

@then('el usuario ve un mensaje de confirmación de envío exitoso')
def step_impl(context):
    assert "Mensaje enviado" in context.browser.page_source, "El usuario no vio el mensaje de confirmación de envío"
    context.screenshot_path = capture_screenshot(context, 'confirmacion_envio')

@then('el usuario ve un mensaje de confirmación de envío exitoso por WhatsApp')
def step_impl(context):
    assert "Mensaje enviado por WhatsApp" in context.browser.page_source, "El usuario no vio el mensaje de confirmación de envío por WhatsApp"
    context.screenshot_path = capture_screenshot(context, 'confirmacion_envio_whatsapp')

@then('el sistema muestra un mensaje de error solicitando llenar todos los campos')
def step_impl(context):
    assert "Por favor, complete todos los campos" in context.browser.page_source, "No se mostró el mensaje de error"
    context.screenshot_path = capture_screenshot(context, 'error_campos_vacios')

@then('el sistema muestra un mensaje de error solicitando llenar todos los campos antes de enviar por WhatsApp')
def step_impl(context):
    assert "Por favor, complete todos los campos antes de enviar por WhatsApp" in context.browser.page_source, "No se mostró el mensaje de error para WhatsApp"
    context.screenshot_path = capture_screenshot(context, 'error_campos_vacios_whatsapp')

@then('el sistema muestra un mensaje de error indicando que el nombre es demasiado corto')
def step_impl(context):
    assert "El nombre es demasiado corto" in context.browser.page_source, "No se mostró el mensaje de error de nombre corto"
    context.screenshot_path = capture_screenshot(context, 'error_nombre_corto')

@then('el sistema muestra un mensaje de error indicando que el nombre no debe contener números')
def step_impl(context):
    assert "El nombre no debe contener números" in context.browser.page_source, "No se mostró el mensaje de error por números en el nombre"
    context.screenshot_path = capture_screenshot(context, 'error_nombre_numeros')

@then('el sistema muestra un mensaje de error indicando que el correo electrónico es inválido')
def step_impl(context):
    assert "Correo electrónico inválido" in context.browser.page_source, "No se mostró el mensaje de error por correo inválido"
    context.screenshot_path = capture_screenshot(context, 'error_correo_invalido')

@then('el sistema muestra un mensaje de error indicando que el mensaje es demasiado corto')
def step_impl(context):
    assert "El mensaje es demasiado corto" in context.browser.page_source, "No se mostró el mensaje de error por mensaje corto"
    context.screenshot_path = capture_screenshot(context, 'error_mensaje_corto')

@then('el sistema muestra un mensaje de error indicando que el mensaje excede el número máximo de caracteres permitidos')
def step_impl(context):
    assert "El mensaje excede el número máximo de caracteres" in context.browser.page_source, "No se mostró el mensaje de error por mensaje largo"
    context.screenshot_path = capture_screenshot(context, 'error_mensaje_largo')
