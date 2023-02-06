# #!/bin/bash

#!-------------------------------------- REMOVING FILES IF EXISTS ----------------------------------------
find ./output -name desc.txt -exec rm {} \;
find ./output -name names.txt -exec rm {} \;
find ./output -name prices.txt -exec rm {} \;
#!-------------------------------------- PREPARING THE FILES ----------------------------------------
#remove all blank lines from a txt file
find ./output/*.txt -exec sed -i '/^$/d' {} \;

#remove the first 2 lines of the txt file 
#find ./output/*.txt -exec tail -n +3 {} > ./output/cleaned_1.txt \;
find ./output/*.txt -exec gawk -i inplace 'NR>2' {} \;

#remove tmp file if exist
find ./output -name tmp_man_1.txt -exec rm {} \;
#remove the last 3 rows and save the result in a temporal file
find ./output/*.txt -exec head -n -5 {} > ./output/tmp_man_1.txt \;

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
echo -e $prices > ./output/prices.txt

# #!-------------------------------------- Setting the format: NAME + Description per line -----------
echo "Removing linespaces"

#Reset IFS so that we can see the original output and not a word-per-line
IFS=$tmp_ifs

new_line=
flag_upper=0
file="./output/tmp_cleaned_man_1.txt"
while IFS= read -r line
do
    if [[ ${line:0:1} =~ [[:upper:]] ]];
    then
        if [[ $flag_upper -eq 0 ]] || [[ $line == *"BBQ"* ]];
        then
            new_line+=$line
            let flag_upper=1
        else
            new_line+="\n"
            new_line+=$line
        fi
    else
        new_line+=$line
    fi
done < "$file"

echo -e $new_line > ./output/tmp_cleaned_man_2.txt

#!-------------------------------------- Getting names ---------------------------------------------
echo "Getting names"

flag_no_phila=0
tmp_string=
final_name=
file="./output/tmp_cleaned_man_2.txt"
while IFS= read -r line
do
    uppercase_words=$(echo "$line" | grep -oE '[A-Z]+')

    last_word=$(echo "$uppercase_words" | awk 'END{print}')

    case $last_word in
    "BBQ")
        final_name+="$uppercase_words\n"
    ;;
    "PHILADELPHIA")
        let flag_no_phila=0
        final_name+="$last_word\n"
    ;;
    "ESPECIAL")
        tmp_string+=" $last_word"
        let flag_no_phila=0
        final_name+="$tmp_string\n"
    ;;
    *)
        if [ $flag_no_phila -eq 0 ];
        then
            length=${#uppercase_words}
            # Remove the last two characters by using string slicing
            tmp_string=${uppercase_words:0:length-2}
            let flag_no_phila=1
        else
            #new_string=$tmp_string
            final_name+="$tmp_string\n"
            length=${#uppercase_words}
            # Remove the last two characters by using string slicing
            tmp_string=${uppercase_words:0:length-2}
        fi
    ;;
    esac
done < "$file"
final_name+="$tmp_string\n"
echo -e $final_name > ./output/names.txt

#!-------------------------------------- Getting descriptions --------------------------------------
echo "Getting Descriptions"

perl -p -e 's/[A-Z]{2,}//g;' <  ./output/tmp_cleaned_man_2.txt > ./output/tmp_desc.txt #Removes all uppercase words
sed -i $'s/[^[:alnum:] ]//g' ./output/tmp_desc.txt #removes all special character
sed -i 's/[A-Z] //' ./output/tmp_desc.txt #Removes capital letters that where before a blank
sed -i 's/^\ *//' ./output/tmp_desc.txt #Removes blanks at the beginning of each line

sed -i '/^$/d' ./output/tmp_desc.txt #Removes blank lines
sed -i '/^$/d' ./output/names.txt #Removes blank lines
sed -i '/^$/d' ./output/prices.txt #Removes blank lines

flag=0
file="./output/tmp_desc.txt"
while IFS= read -r line
do
    # Get the first character of the string
    first_char=${line:0:1}

    # Check if the first character is uppercase
    if [[ $first_char == [[:upper:]] ]]; then
        if [ $flag -eq 0 ];
        then
            tmp_string=$line
            let flag=1
        else
            final_line+="$tmp_string\n"
            tmp_string=$line
        fi
    else
        tmp_string+=$line
        final_line+="$tmp_string\n"
        let flag=0
    fi
done < "$file"
final_line+="$tmp_string"
echo -e $final_line > ./output/desc.txt

#!-------------------------------------- Removing all temporal files -------------------------------
echo "Removing temporal files"

rm ./output/man*.txt
rm ./output/tmp_cleaned_man_1.txt
rm ./output/tmp_cleaned_man_2.txt
rm ./output/tmp_man_1.txt
rm ./output/tmp_desc.txt

find ./resources/*.jpg -exec mv {} ./converted/ \;