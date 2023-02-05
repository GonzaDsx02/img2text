# IMAGE TO TEXT CONVERTER

## Getting Started
### Install Tesseract-OCR before running

    [Tesseract-OCR](https://github.com/tesseract-ocr/tessdoc#binaries)

    pip install pytesseract
    pip install Pillow

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
### Pass python version as an argument
You can pass the python version to the run.sh script as well.

    version=$1
    client=$2
    type=$3

    $version src/python/img2text.py $client $type

Running example:

    python3 run.sh man f