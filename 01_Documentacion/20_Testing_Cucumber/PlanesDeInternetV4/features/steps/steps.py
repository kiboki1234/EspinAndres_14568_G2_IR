from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# URL base de la página web de prueba
BASE_URL = 'https://pagina-testing-dusky.vercel.app/'

@given('el usuario accede a la página de INPACTONET')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get(BASE_URL)
    context.browser.maximize_window()
    time.sleep(2)

@when('el usuario visualiza los planes de Internet disponibles')
def step_impl(context):
    context.plans = context.browser.find_elements(By.CLASS_NAME, 'plan')
    assert len(context.plans) > 0, "No se encontraron planes de Internet"
    context.screenshot_path = capture_screenshot(context, 'visualiza_planes')

@then('el usuario debe ver el ancho de banda en la parte superior de cada plan')
def step_impl(context):
    for plan in context.plans:
        assert plan.find_element(By.CLASS_NAME, 'bandwidth').is_displayed(), "No se encontró el ancho de banda en un plan"
    context.screenshot_path = capture_screenshot(context, 'ancho_de_banda')

@then('el usuario debe ver una imagen representativa de cada plan')
def step_impl(context):
    for plan in context.plans:
        assert plan.find_element(By.CLASS_NAME, 'plan-image').is_displayed(), "No se encontró la imagen representativa en un plan"
    context.screenshot_path = capture_screenshot(context, 'imagen_representativa')

@then('el usuario debe ver una breve descripción del plan de Internet')
def step_impl(context):
    for plan in context.plans:
        assert plan.find_element(By.CLASS_NAME, 'description').is_displayed(), "No se encontró la descripción corta en un plan"
    context.screenshot_path = capture_screenshot(context, 'descripcion_corta')

@then('el usuario debe ver un botón etiquetado como "Cotizar" en cada plan')
def step_impl(context):
    for plan in context.plans:
        assert plan.find_element(By.CLASS_NAME, 'quote-button').is_displayed(), "No se encontró el botón de cotización en un plan"
    context.screenshot_path = capture_screenshot(context, 'boton_cotizar')

@when('el usuario selecciona un plan específico')
def step_impl(context):
    context.plans[0].find_element(By.CLASS_NAME, 'quote-button').click()
    time.sleep(2)
    context.screenshot_path = capture_screenshot(context, 'seleccionar_plan')

@then('el usuario es redirigido a la página de contacto')
def step_impl(context):
    assert "contact.html" in context.browser.current_url, "No se redirigió a la página de contacto"
    context.screenshot_path = capture_screenshot(context, 'pagina_contacto')

@then('el usuario llena el formulario de contacto')
def step_impl(context):
    context.browser.find_element(By.NAME, 'name').send_keys('Test User')
    context.browser.find_element(By.NAME, 'email').send_keys('test.com')
    context.browser.find_element(By.NAME, 'message').send_keys('Estoy interesado en el plan de Internet.')
    context.browser.find_element(By.ID, 'submit-button').click()
    time.sleep(2)
    context.screenshot_path = capture_screenshot(context, 'llenar_formulario')


@then('el sistema envía el mensaje del usuario a la secretaria')
def step_impl(context):
    # Simula la acción de enviar el mensaje y recibir la confirmación
    assert "Mensaje enviado" in context.browser.page_source, "El mensaje no se envió correctamente"
    context.screenshot_path = capture_screenshot(context, 'mensaje_enviado')

@then('la secretaria recibe el mensaje del sistema')
def step_impl(context):
    # Simula la acción de recepción del mensaje por parte de la secretaria
    pass

@then('la secretaria responde el mensaje de acuerdo con la información solicitada')
def step_impl(context):
    # Simula la acción de respuesta de la secretaria
    pass

@then('el sistema envía la respuesta de la secretaria al usuario')
def step_impl(context):
    # Simula la acción de enviar la respuesta de la secretaria al usuario
    pass

@then('se establece comunicación entre la secretaria y el usuario')
def step_impl(context):
    # Verifica que la comunicación se estableció
    pass

@then('el usuario no debe ver ningún plan de Internet')
def step_impl(context):
    assert len(context.plans) == 0, "Se encontraron planes de Internet cuando no debería haber ninguno"
    context.screenshot_path = capture_screenshot(context, 'no_planes')

@then('el usuario no puede seleccionar ningún plan')
def step_impl(context):
    assert all(not plan.find_element(By.CLASS_NAME, 'quote-button').is_displayed() for plan in context.plans), "Se puede seleccionar un plan cuando no debería ser posible"
    context.screenshot_path = capture_screenshot(context, 'no_seleccionar_plan')

@then('el usuario no debe ver el ancho de banda en los planes')
def step_impl(context):
    assert all(not plan.find_element(By.CLASS_NAME, 'bandwidth').is_displayed() for plan in context.plans), "Se muestra el ancho de banda cuando no debería ser visible"
    context.screenshot_path = capture_screenshot(context, 'no_ancho_de_banda')

@then('el usuario no es redirigido a la página de contacto')
def step_impl(context):
    assert "contact.html" not in context.browser.current_url, "Se redirigió a la página de contacto cuando no debería haber sucedido"
    context.screenshot_path = capture_screenshot(context, 'no_redirigido_contacto')

@then('el sistema no envía el mensaje del usuario a la secretaria')
def step_impl(context):
    assert "Mensaje enviado" not in context.browser.page_source, "El mensaje fue enviado cuando no debería haber sido"
    context.screenshot_path = capture_screenshot(context, 'no_mensaje_enviado')

@then('la secretaria no recibe el mensaje del sistema')
def step_impl(context):
    # Simula la acción de que la secretaria no recibe el mensaje
    pass

def capture_screenshot(context, name):
    screenshot_path = f'screenshots/{name}.png'
    context.browser.save_screenshot(screenshot_path)
    return screenshot_path
