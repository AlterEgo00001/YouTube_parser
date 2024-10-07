from docx import Document
from docx.shared import Inches
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import logging

logging.basicConfig(level=logging.DEBUG)

def generate_docx(text_image_pairs, output_path):
    """Создаёт документ в формате DOCX с текстом и изображениями"""
    try:
        doc = Document()
        for image, text in text_image_pairs:
            # Преобразуем изображение в байты для вставки
            doc.add_paragraph(text)
        doc.save(output_path)
        logging.debug(f"DOCX saved to {output_path}")
    except Exception as e:
        logging.error(f"Error generating DOCX: {e}")

def generate_pdf(text_image_pairs, output_path):
    """Создаёт PDF документ с текстом и изображениями"""
    try:
        c = canvas.Canvas(output_path, pagesize=letter)
        width, height = letter
        for image, text in text_image_pairs:
            c.drawImage(image, 0, height // 2, width, height // 2)
            c.drawString(100, height // 2 - 50, text)
            c.showPage()
        c.save()
        logging.debug(f"PDF saved to {output_path}")
    except Exception as e:
        logging.error(f"Error generating PDF: {e}")
