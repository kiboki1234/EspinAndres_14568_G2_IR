from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

BASE_URL = 'https://pagina-testing-dusky.vercel.app/'

def capture_screenshot(context, name):
    screenshot_path = f'screenshots/{name}.png'
    context.browser.save_screenshot(screenshot_path)
    context.screenshot_path = screenshot_path
    return screenshot_path

@given('el usuario accede a la página de IMPACTONET')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get(BASE_URL)
    context.browser.maximize_window()
    context.screenshot_path = capture_screenshot(context, 'Ingreso_a_IMPACTONET')
    time.sleep(2)

@when('el usuario se dirige al apartado de "Acerca de Nosotros"')
def step_impl(context):
    context.browser.find_element(By.LINK_TEXT, 'Acerca de Nosotros').click()
    time.sleep(2)
    context.screenshot_path = capture_screenshot(context, 'Acerca_de_Nosotros')

@then('el sistema despliega la información sobre la misión y visión de la empresa')
def step_impl(context):
    mission_vision_text = context.browser.find_element(By.ID, 'mission-vision').text
    assert "Misión" in mission_vision_text and "Visión" in mission_vision_text, "No se encontró la misión y visión de la empresa"
    context.screenshot_path = capture_screenshot(context, 'Mision_Vision')

@when('el usuario presiona el botón "Hablar con Nosotros"')
def step_impl(context):
    context.browser.find_element(By.ID, 'contact-button').click()
    time.sleep(2)
    context.screenshot_path = capture_screenshot(context, 'Hablar_con_Nosotros')

@then('el sistema no redirige a ninguna página')
def step_impl(context):
    current_url = context.browser.current_url
    assert current_url == f'{BASE_URL}AcercadeNosotros.html', "El sistema redirigió a otra página"
    context.screenshot_path = capture_screenshot(context, 'No_Redirigido')

@then('el usuario ve un mensaje de error o un mensaje de que la página no está disponible')
def step_impl(context):
    error_message = context.browser.find_element(By.ID, 'error-message').text
    assert "Página no disponible" in error_message or "Error" in error_message, "No se mostró el mensaje de error"
    context.screenshot_path = capture_screenshot(context, 'Error_Message')

@then('el sistema redirige al usuario a la página de contacto')
def step_impl(context):
    current_url = context.browser.current_url
    assert current_url == f'{BASE_URL}contacto.html', "El sistema no redirigió a la página de contacto"
    context.screenshot_path = capture_screenshot(context, 'Pagina_Contacto')

@then('el sistema muestra el formulario de contacto para que el usuario lo llene')
def step_impl(context):
    assert context.browser.find_element(By.ID, 'contact-form').is_displayed(), "No se encontró el formulario de contacto"
    context.screenshot_path = capture_screenshot(context, 'Formulario_Contacto')

@when('el usuario se dirige al sub-apartado de "Trabajos Realizados"')
def step_impl(context):
    context.browser.find_element(By.LINK_TEXT, 'Trabajos Realizados').click()
    time.sleep(2)
    # Hacer scroll hasta el final de la página
    context.browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(2)
    context.screenshot_path = capture_screenshot(context, 'Trabajos_Realizados')

@then('el sistema intenta cargar las imágenes y descripciones de los trabajos realizados')
def step_impl(context):
    # Se espera que las imágenes y descripciones tengan una clase común
    trabajos = context.browser.find_elements(By.CLASS_NAME, 'trabajo-realizado')
    assert trabajos, "No se encontraron trabajos realizados"
    context.screenshot_path = capture_screenshot(context, 'Cargar_Trabajos')

@then('el sistema no muestra ninguna imagen ni descripción')
def step_impl(context):
    trabajos = context.browser.find_elements(By.CLASS_NAME, 'trabajo-realizado')
    for trabajo in trabajos:
        assert not trabajo.find_element(By.TAG_NAME, 'img').is_displayed(), "Se mostró una imagen"
        assert not trabajo.find_element(By.TAG_NAME, 'p').is_displayed(), "Se mostró una descripción"
    context.screenshot_path = capture_screenshot(context, 'No_Imagenes_Descripciones')

@then('el usuario ve un mensaje de error indicando que no se pueden cargar los trabajos realizados')
def step_impl(context):
    error_message = context.browser.find_element(By.ID, 'error-trabajos').text
    assert "No se pueden cargar los trabajos realizados" in error_message, "No se mostró el mensaje de error"
    context.screenshot_path = capture_screenshot(context, 'Error_Cargar_Trabajos')

@then('el sistema carga las imágenes y descripciones de los trabajos realizados')
def step_impl(context):
    trabajos = context.browser.find_elements(By.CLASS_NAME, 'trabajo-realizado')
    for trabajo in trabajos:
        assert trabajo.find_element(By.TAG_NAME, 'img').is_displayed(), "No se mostró una imagen"
        assert trabajo.find_element(By.TAG_NAME, 'p').is_displayed(), "No se mostró una descripción"
    context.screenshot_path = capture_screenshot(context, 'Cargar_Trabajos_Exito')

@then('el usuario puede ver las imágenes y leer las descripciones de cada trabajo realizado')
def step_impl(context):
    trabajos = context.browser.find_elements(By.CLASS_NAME, 'trabajo-realizado')
    for trabajo in trabajos:
        assert trabajo.find_element(By.TAG_NAME, 'img').is_displayed(), "No se mostró una imagen"
        assert trabajo.find_element(By.TAG_NAME, 'p').is_displayed(), "No se mostró una descripción"
    context.screenshot_path = capture_screenshot(context, 'Ver_Trabajos')

@then('el sistema permite navegar por los trabajos realizados mediante un carrusel interactivo')
def step_impl(context):
    assert context.browser.find_element(By.ID, 'trabajos-carousel').is_displayed(), "No se mostró el carrusel interactivo"
    context.screenshot_path = capture_screenshot(context, 'Carrusel_Interactivo')
