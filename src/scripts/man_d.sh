find ./output -name desc.txt -exec rm {} \;
find ./output -name names.txt -exec rm {} \;
find ./output -name prices.txt -exec rm {} \;

#remove the first 3 lines of the txt file 
find ./output/*.txt -exec gawk -i inplace 'NR>4' {} \;

#get content of all .txt files and save the result in a temporal file
find ./output/*.txt -exec head -n -0 {} > ./output/tmp_man_1.txt \;

#remove all blank lines from a txt file
find ./output/*.txt -exec sed -i '/^$/d' {} \;

#!-------------------------------------- REMOVING DOLLAR AND PRICE ---------------------------------
echo "Removing dollar sign and prices"

single_line=
prices=

#Backup of IFS to reset it later
tmp_ifs=$IFS
IFS='$'
file="./output/tmp_man_1.txt"
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
echo -e $single_line > ./output/tmp_cleaned_man_1.txt
echo -e $prices > ./output/tmp_prices.txt

#remove the first 3 lines of the txt file 
find ./output/tmp_prices.txt -exec head -n -3 {} > ./output/prices.txt \;

#remove all blank lines from a txt file
find ./output/tmp_cleaned_man_1.txt -exec sed -i '/^$/d' {} \;

rm ./output/tmp_man_1.txt
rm ./output/tmp_prices.txt

# #!-------------------------------------- Setting the format: NAME + Description per line -----------
echo "Removing linespaces"

#Reset IFS so that we can see the original output and not a word-per-line
IFS=$tmp_ifs

new_line=
flag_upper=0
fl_exit=0
file="./output/tmp_cleaned_man_1.txt"
while IFS= read -r line
do
    if [[ $line =~ "POSTRES" ]];
    then
        break
    else
        if [[ ! $line =~ [[:lower:]] ]];
        then
            if [[ $flag_upper -eq 0 ]];
            then
                new_line+="$line |"
                let flag_upper=1
            else
                new_line+=" \n"
                new_line+="$line |"
            fi
        else
            new_line+="$line"
        fi
    fi
done < "$file"

echo -e $new_line > ./output/tmp_names_descriptions.txt

find ./output/*.txt -name tmp_names_descriptions.txt -exec sed 's/,/ /g' {} > output/names_descriptions.txt \; 

rm ./output/tmp_names_descriptions.txt
rm ./output/tmp_cleaned_man_1.txt
rm ./output/man*.txt

find ./resources/*.jpg -exec mv {} ./converted/ \;