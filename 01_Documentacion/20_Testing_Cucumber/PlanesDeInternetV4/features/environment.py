from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Reporte de Pruebas de Planes de Internet", 0, 1, "C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, title, 0, 1, "L")
        self.ln(5)

    def step_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, 0, 1, "L")
        self.ln(5)

    def step_status(self, status):
        self.set_font("Arial", "B", 10)
        if status == 'passed':
            self.set_text_color(0, 128, 0)  # Verde para paso exitoso
        else:
            self.set_text_color(255, 0, 0)  # Rojo para fallo
        self.cell(0, 10, f"Status: {status}", 0, 1, "L")
        self.set_text_color(0, 0, 0)  # Negro para texto normal
        self.ln(2)

    def step_screenshot(self, image_path):
        self.image(image_path, x=10, y=None, w=190)
        self.ln(85)

def before_all(context):
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
    if not os.path.exists('Evidencias'):
        os.makedirs('Evidencias')

def before_scenario(context, scenario):
    context.pdf = PDF()
    context.pdf.add_page()
    context.pdf.chapter_title(f"Scenario: {scenario.name}")

def after_step(context, step):
    context.pdf.step_title(f"Step: {step.name}")
    context.pdf.step_status(step.status)
    if hasattr(context, 'screenshot_path'):
        context.pdf.step_screenshot(context.screenshot_path)

def after_scenario(context, scenario):
    if hasattr(context, 'browser'):
        context.browser.quit()
    # Guardar el PDF al final del escenario
    pdf_filename = f"Evidencias/{scenario.name}.pdf"
    context.pdf.output(pdf_filename)

def after_all(context):
    pass
