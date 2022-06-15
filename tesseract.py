import pandas as pd
import pytesseract
import openpyxl

try:
    from PIL import Image
except ImportError:
    import Image
pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename), lang='rus')
    return text
