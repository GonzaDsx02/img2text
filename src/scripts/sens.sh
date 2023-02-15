#!/bin/bash

#!-------------------------------------- REMOVING FILES IF EXISTS ----------------------------------------
find ./output -name desc.txt -exec rm {} \;
find ./output -name names.txt -exec rm {} \;
find ./output -name prices.txt -exec rm {} \;

#remove all blank lines from a txt file
find ./output/*.txt -exec sed -i '/^$/d' {} \;

#remove the first 2 lines of the txt file 
find ./output/*.txt -exec gawk -i inplace 'NR>4' {} \;

#remove the last 3 rows and save the result in a temporal file
find ./output/*.txt -exec head -n -2 {} > ./output/tmp_sens_1.txt \;

#!-------------------------------------- REMOVING DOLLAR AND PRICE ---------------------------------
echo "Removing dollar sign and prices"

single_line=
prices=

#Backup of IFS to reset it later
tmp_ifs=$IFS
IFS='$'
file="./output/tmp_sens_1.txt"
while IFS= read -r line
do
    if [[ $line == *"$"* ]]; 
    then
        #Read the split words into an array based on space delimiter
        read -a strarr <<< "$line"
        single_line+="${line%\$*}\n"
        prices+="${strarr[1]}\n"
    else
        single_line+="${line}\n"
    fi
done < "$file"
echo -e $single_line > ./output/tmp_cleaned_sens_1.txt
echo -e $prices > ./output/tmp_prices.txt