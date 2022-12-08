import os
from PIL import Image
from pytesseract import *

folder = 'D:/ING EN SISTEMAS/Residencia/resources/'
with os.scandir(folder) as files:
    n = 1
    for file in files:
        
        # convert the img to text
        print(f"procesing {file}")
        pytesseract.tesseract_cmd = r'D:\Pytesseract\tesseract.exe'
        img = Image.open(folder+file.name)
        lines = pytesseract.image_to_string(img)
        
        # saves the output in output.txt file
        name = f"output{n}.txt"
        with open(name, 'w') as f:
            for line in lines:
                f.write(line)
                #f.write('\n')
        n+=1
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