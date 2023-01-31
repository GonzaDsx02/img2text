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

client = ""
menu_type = ""
rsrc_path = 'resources/'
output_path = 'output/'
clients = ["man", "sens", "sone", "fushi"]
menuTypes = ["f", "d"]
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
    print("\nCONVERTION SUCCEDED!\n")

def filter():
    for i,file in enumerate(output_files):
        res=""
        print(f"cleanning {files[i].name}")
        with open(file) as f:
            for line in f:
                if "$" in line:
                    res += line
        f.close()
        with open(file, 'w') as f:
            f.write(res)
        #print(res)
    print("\nFILTER 1 SUCCEDED!\n")

def validateArguments():
    if len(sys.argv) == 3:
        global client
        global menu_type
        client = sys.argv[1]
        menu_type = sys.argv[2]
        if client not in clients:
            raise Exception("Client not found")
        if menu_type not in menuTypes:
            raise Exception("Invalid type of menu\nInsert \'d\' for drinks or \'f\' for food")
    else:
        print("Error - Missing arguments. (add <client> or <menu_type>)")
        print('EX: python img2text.py restaurant1 food')
        raise Exception("Invalid arguments")


#Usage: python img2text.py <client> <type>
def main():
    try:
        validateArguments()
        print(f"Starting process for client={client} and type={menu_type}")
        
        print("Starting converter")
        convert()
        
        #filter1()
        print("Starting filters")
    except Exception as e:
        print(e)
        print("\nSystem exit with error 1")

if __name__ == "__main__":
    main()