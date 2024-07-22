import os
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Crear una carpeta para guardar las evidencias
if not os.path.exists("Evidencias"):
    os.makedirs("Evidencias")

# Función para guardar una captura de pantalla
def save_screenshot(driver, filename):
    screenshot_path = os.path.join("Evidencias", filename)
    driver.save_screenshot(screenshot_path)
    return screenshot_path

# Función para agregar una imagen a un archivo PDF
def add_image_to_pdf(pdf, image_path, step_name, status):
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Step: {step_name} - Status: {status}", ln=True)
    pdf.image(image_path, x=10, y=20, w=190)
    pdf.ln(85)

@given('el usuario accede a la página de IMPACTONET')
def step_user_visits_impactonet(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("https://pagina-testing-dusky.vercel.app/")  # Actualiza esta ruta con la ruta correcta
    screenshot_path = save_screenshot(context.driver, 'step_user_visits_impactonet.png')
    add_image_to_pdf(context.pdf, screenshot_path, 'el usuario accede a la página de IMPACTONET', 'passed')

@when('el sistema muestra los planes de internet disponibles')
def step_system_displays_internet_plans(context):
    screenshot_path = save_screenshot(context.driver, 'step_system_displays_internet_plans.png')
    add_image_to_pdf(context.pdf, screenshot_path, 'el sistema muestra los planes de internet disponibles', 'passed')

@then('el usuario debe ver el ancho de banda en la parte superior de cada plan')
def step_user_sees_bandwidth(context):
    bandwidth_elements = context.driver.find_elements(By.CLASS_NAME, "bandwidth")
    for element in bandwidth_elements:
        assert element.is_displayed()
    screenshot_path = save_screenshot(context.driver, 'step_user_sees_bandwidth.png')
    add_image_to_pdf(context.pdf, screenshot_path, 'el usuario debe ver el ancho de banda en la parte superior de cada plan', 'passed')

@then('el usuario debe ver una imagen representativa de cada plan')
def step_user_sees_image(context):
    image_elements = context.driver.find_elements(By.CLASS_NAME, "plan-image")
    for element in image_elements:
        assert element.is_displayed()
    screenshot_path = save_screenshot(context.driver, 'step_user_sees_image.png')
    add_image_to_pdf(context.pdf, screenshot_path, 'el usuario debe ver una imagen representativa de cada plan', 'passed')

@then('el usuario debe ver una breve descripción del plan de internet')
def step_user_sees_description(context):
    description_elements = context.driver.find_elements(By.CLASS_NAME, "description")
    for element in description_elements:
        assert element.is_displayed()
    screenshot_path = save_screenshot(context.driver, 'step_user_sees_description.png')
    add_image_to_pdf(context.pdf, screenshot_path, 'el usuario debe ver una breve descripción del plan de internet', 'passed')

@then('el usuario debe ver un botón etiquetado como "Cotizar" en cada plan')
def step_user_sees_quote_button(context):
    quote_button_elements = context.driver.find_elements(By.CLASS_NAME, "quote-button")
    for element in quote_button_elements:
        assert element.text == "Cotizar"
    screenshot_path = save_screenshot(context.driver, 'step_user_sees_quote_button.png')
    add_image_to_pdf(context.pdf, screenshot_path, 'el usuario debe ver un botón etiquetado como "Cotizar" en cada plan', 'passed')

@given('el usuario está en la página de IMPACTONET')
def step_user_on_impactonet_page(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("https://pagina-testing-dusky.vercel.app/")
    screenshot_path = save_screenshot(context.driver, 'step_user_on_impactonet_page.png')
    add_image_to_pdf(context.pdf, screenshot_path, 'el usuario está en la página de IMPACTONET', 'passed')

@when('el usuario selecciona un plan específico')
def step_user_selects_plan(context):
    plan = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "plan1"))
    )
    context.driver.execute_script("arguments[0].scrollIntoView();", plan)
    quote_button = WebDriverWait(plan, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "quote-button"))
    )
    context.driver.execute_script("arguments[0].scrollIntoView();", quote_button)
    actions = ActionChains(context.driver)
    actions.move_to_element(quote_button).click().perform()
    screenshot_path = save_screenshot(context.driver, 'step_user_selects_plan.png')
    add_image_to_pdf(context.pdf, screenshot_path, 'el usuario selecciona un plan específico', 'passed')

@then('el sistema debe redirigir al usuario a la página de contacto')
def step_system_redirects_to_contact(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("contact.html")
    )
    assert "contact.html" in context.driver.current_url
    screenshot_path = save_screenshot(context.driver, 'step_system_redirects_to_contact.png')
    add_image_to_pdf(context.pdf, screenshot_path, 'el sistema debe redirigir al usuario a la página de contacto', 'passed')

@then('el usuario debe poder llenar el formulario de contacto')
def step_user_fills_contact_form(context):
    contact_form = context.driver.find_element(By.ID, "contact-form")
    assert contact_form.is_displayed()
    screenshot_path = save_screenshot(context.driver, 'step_user_fills_contact_form.png')
    add_image_to_pdf(context.pdf, screenshot_path, 'el usuario debe poder llenar el formulario de contacto', 'passed')

@then('el usuario debe poder enviar el formulario de contacto')
def step_user_submits_contact_form(context):
    submit_button = context.driver.find_element(By.ID, "submit-button")
    submit_button.click()
    screenshot_path = save_screenshot(context.driver, 'step_user_submits_contact_form.png')
    add_image_to_pdf(context.pdf, screenshot_path, 'el usuario debe poder enviar el formulario de contacto', 'passed')
