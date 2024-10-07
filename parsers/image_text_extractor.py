import cv2
import pytesseract
from pytesseract import Output

def extract_text_from_image(image):
    return pytesseract.image_to_string(image, output_type=Output.DICT)

def associate_text_with_images(frames):
    text_image_pairs = []
    for frame in frames:
        text = extract_text_from_image(frame)
        if text:
            text_image_pairs.append((frame, text))
    return text_image_pairs
