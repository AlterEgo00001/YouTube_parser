import cv2
import pytesseract
from pytesseract import Output
import logging

logging.basicConfig(level=logging.DEBUG)

def extract_text_from_image(image):
    """Извлекает текст из изображения, используя pytesseract"""
    try:
        return pytesseract.image_to_string(image, output_type=Output.DICT)
    except Exception as e:
        logging.error(f"Error extracting text from image: {e}")
        return {}

def associate_text_with_images(frames):
    """Ассоциирует текст с изображениями"""
    text_image_pairs = []
    for i, frame in enumerate(frames):
        text = extract_text_from_image(frame)
        if text.get('text'):
            text_image_pairs.append((frame, text['text']))
            logging.debug(f"Text extracted from frame {i}: {text['text'][:50]}...")
        else:
            logging.debug(f"No text found in frame {i}")
    return text_image_pairs
