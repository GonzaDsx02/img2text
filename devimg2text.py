from PIL import Image
from pytesseract import *

pytesseract.tesseract_cmd = r'D:\Pytesseract\tesseract.exe'
img = Image.open("D:/ING EN SISTEMAS/Residencia/resources/menu2.jpg")
resultado = pytesseract.image_to_string(img)
print(resultado)