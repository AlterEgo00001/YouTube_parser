from docx import Document
from docx.shared import Inches
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def generate_docx(text_image_pairs, output_path):
    doc = Document()
    for image, text in text_image_pairs:
        doc.add_picture(image, width=Inches(5.0))
        doc.add_paragraph(text)
    doc.save(output_path)

def generate_pdf(text_image_pairs, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    for image, text in text_image_pairs:
        c.drawImage(image, 0, height // 2, width, height // 2)
        c.drawString(100, height // 2 - 50, text)
        c.showPage()
    c.save()
