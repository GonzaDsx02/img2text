import os
folder = 'D:/ING EN SISTEMAS/Residencia/resources'
with os.scandir(folder) as files:
    if(files == 0):
        print("error")
    else:
        print("cool")