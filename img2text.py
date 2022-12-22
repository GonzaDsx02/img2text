import os
from PIL import Image
from pytesseract import *
import subprocess
import pyocr
import pyocr.builders
import io
import sys
import re

#!------------------------------ starter functions ------------------------------

def getFiles():
    arr = []
    with os.scandir(rsrc_path) as files:
        for file in files:
            arr.append(file)
    return arr

#!------------------------------ global variables ------------------------------

tool = pyocr.get_available_tools()[0]
lang = 'spa'
rsrc_path = 'D:/ING EN SISTEMAS/Residencia/resources/'
output_path = 'D:/ING EN SISTEMAS/Residencia/crawler_python/output/'
files = getFiles()
output_files = []

#used to remove the file extension while saving the txt. EX sushi.png -> sushi
def second_group(m):
    return m.group(1)

def convert():
    for file in files:
        # convert the img to text
        print(f"procesing {file.name}")
        pytesseract.tesseract_cmd = r'D:\Pytesseract\tesseract.exe'
        img = Image.open(rsrc_path+file.name)
        lines = pytesseract.image_to_string(img)
        name = re.sub("(.*)(.{3}$)", second_group, file.name)

        # saves the output in output.txt file
        name = output_path+f"{name}txt"
        output_files.append(name)
        with open(name, 'w') as f:
            for line in lines:
                f.write(line)
    print("Done!")

def filter1():
    for i,file in enumerate(output_files):
        print(i)
        res=""
        print(file)
        with open(file) as f:
            for line in f:
                if "$" in line:
                    res += line
        f.close()
        with open(file, 'w') as f:
            f.write(res)
        #print(res)
        print("done")

convert()
filter1()