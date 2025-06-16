# export.py

from fpdf import FPDF
from io import BytesIO

class CarePlanPDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 16)
        self.cell(0, 10, 'Care Plan', ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

def generate_pdf(plan_dict: dict)-> bytes:
    pdf = CarePlanPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    def write_section_title(title):
        pdf.set_font("Arial", 'B', 14)
        pdf.set_text_color(30, 30, 30)
        pdf.cell(0, 10, f"{title}", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.set_text_color(0, 0, 0)

    def write_item(text):
        # Ensures long content wraps
        pdf.multi_cell(0, 8, f"- {text}", align='L')
        pdf.ln(1)

    for section, items in plan_dict.items():
        write_section_title(section.capitalize())
        if not items:
            write_item("No entries.")
            continue

        for item in items:
            if isinstance(item, dict):
                line = "; ".join(f"{k}: {v}" for k, v in item.items())
            else:
                line = str(item)
            write_item(line)

        pdf.ln(5)

    # Save as in-memory buffer
    buffer = BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer.read()
