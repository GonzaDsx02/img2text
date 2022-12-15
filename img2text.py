import os
from PIL import Image
from pytesseract import *
import subprocess
import pyocr
import pyocr.builders
import io
import sys
import re

tool = pyocr.get_available_tools()[0]
lang = 'spa'

#used to remove the file extension while saving the txt. EX sushi.png -> sushi
def second_group(m):
    return m.group(1)

folder = 'D:/ING EN SISTEMAS/Residencia/resources/'
with os.scandir(folder) as files:
    n = 1
    for file in files:

        # convert the img to text
        print(f"procesing {file.name}")
        pytesseract.tesseract_cmd = r'D:\Pytesseract\tesseract.exe'
        img = Image.open(folder+file.name)
        lines = pytesseract.image_to_string(img)
        name = re.sub("(.*)(.{3}$)", second_group, file.name)
        # saves the output in output.txt file
        name = f"{name}txt"
        with open(name, 'w') as f:
            for line in lines:
                f.write(line)
        n+=1
    #subprocess.call(['sh', './text.sh'])
    print("Done!")



# Comprobación de seguridad, ejecutar sólo si se reciben 2 argumentos reales
# if len(sys.argv) == 3:
#     texto = sys.argv[1]
#     repeticiones = int(sys.argv[2])
#     for r in range(repeticiones):
#         print(texto)
# else:
#     print("Error - Introduce los argumentos correctamente")
#     print('Ejemplo: escribir_lineas.py "Texto" 5')