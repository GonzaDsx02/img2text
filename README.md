# IMAGE TO TEXT CONVERTER

## Getting Started
### Install Tesseract-OCR before running

[Tesseract-OCR](https://github.com/tesseract-ocr/tessdoc/blob/main/Installation.md#installation)

## After-install settings:

### set installation URL in the project's .env file
    [OCR]
    URL=D:\Pytesseract\tesseract.exe (Your URL here)

### Install required pip libraries:
    pip install pytesseract
    pip install Pillow
    pip install pyocr

## Execute run.sh TO CONVERT MENU IMAGES TO TEXT.

    ./run.sh <client> <type>

### Example:

    ./run.sh man f

## INFO:

### Arguments

    <client> can be one of the followings (ONLY ONE):

    * man 
    * sens 
    * sone
    * fushi
    (Customer names have been changed due to copyright issues)

    <type> could be "f" or "d" (making reference to food or drink menu types)

## Run with another version of python
### Get your installed python version:

    1. Using sys. version method.
    2. Using python_version() function.
    3. Using Python -V command.

### Update run.sh script:
Set static version of python

    client=$1
    type=$2

    <python_version> src/python/img2text.py $client $type

Run normally as 

    ./run.sh <client> <type>