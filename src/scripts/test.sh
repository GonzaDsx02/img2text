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
                new_line+="$line | "
                let flag_upper=1
            else
                new_line+=" \n"
                new_line+="$line | "
            fi
        else
            new_line+="$line"
        fi
    fi
done < "$file"

echo -e $new_line > ./output/tmp_cleaned_man_2.txt