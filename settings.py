import os
from decouple import config

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

PHANTOMJS_DRIVER = config('PHANTOMJS_DRIVER', default=r'C:\phantomjs\bin\phantomjs.exe')
SCREENSHOT_PATH = os.path.join(ROOT_DIR, 'captchas')
PYTESSERACT_PATH = config('PYTESSERACT_PATH', default=r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe')

