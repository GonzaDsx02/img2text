import os
import io
import sys
import re
import subprocess
import csv 
import pyocr
import configparser
import pyocr.builders
from PIL import Image
from pytesseract import *

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
rsrc_path = './resources/'
output_path = './output/'
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
        config = configparser.ConfigParser()
        config.read('.env')
        inst=config.get('OCR','URL')
        pytesseract.tesseract_cmd = r''+inst
        img = Image.open(rsrc_path+file.name)
        lines = pytesseract.image_to_string(img)
        name = re.sub("(.*)(.{3}$)", second_group, file.name)

        # saves the output in .txt file
        name = output_path+f"{name}txt"
        output_files.append(name)
        with open(name, 'w') as f:
            for line in lines:
                f.write(line)
    print("\nCONVERTION SUCCEDED!\n")

def exportData(client, menu_type):
    if (client == "man" and menu_type == "f"):        
        #subprocess.call(['sh', './src/scripts/man.sh'])
        rows =[]
        names = open('./output/names.txt','r').read().splitlines()
        desc = open('./output/desc.txt','r').read().splitlines()
        prices = open('./output/prices.txt','r').read().splitlines()
        for i, n in enumerate(names):
            rows.append({"Name":n, "Description":desc[i], "Price":prices[i]})
        #print(rows)
        createCsv(rows, client, menu_type)
        subprocess.call(['sh', './deleteoutput.sh'])
    elif (client == "man" and menu_type == "d"):
        subprocess.call(['sh', './src/scripts/man_d.sh'])
        rows =[]
        prods = open('./output/names_descriptions.txt','r').read().splitlines()
        prices = open('./output/prices.txt','r').read().splitlines()
        for i, prod in enumerate(prods):
            cols = prod.split("|")
            rows.append({"Name":cols[0], "Description":cols[1], "Price":prices[i]})
        createCsv(rows)
        subprocess.call(['sh', './deleteoutput.sh'])
    elif client == "sens":
        print("Comming soon")
    elif client == "sone":
        print("Comming soon")
    elif client == "fushi":
        print("Comming soon")
    else:
        print(f"We dont have an script to clean files of this client ${client}")

def createCsv(rows, client, menu_type):
    # field names 
    output_name=f"products_{client}_{menu_type}"
    fields = ['Name', 'Description', 'Price'] 
    with open(f'./output/{output_name}.csv', 'w', newline='') as file: 
        writer = csv.DictWriter(file, fieldnames = fields)
        writer.writeheader() 
        writer.writerows(rows)

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
        print('EX: python img2text.py restaurant1 f')
        raise Exception("Invalid arguments")

#Usage: python img2text.py <client> <type>
def main():
    try:
        validateArguments()
        print(f"Starting process for client={client} and type={menu_type}")
        
        print("Starting converter")
        convert()
        
        #print("Starting filter script")
        #clean()

        # #add output to csv file here

        print("\nFiles converted successfully\n")
        #print(config.get('OCR','URL'))
    except Exception as e:
        print(e)
        print("\nSystem exit with error 1")

if __name__ == "__main__":
    main()