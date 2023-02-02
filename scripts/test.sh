flag=0
file="./output/tmp_desc.txt"
while IFS= read -r line
do
    #echo $line
    # Get the first character of the string
    first_char=${line:0:1}
    echo $first_char
    # Check if the first character is uppercase
    # Check if the character is uppercase
    if [[ $first_char == [[:lower:]] ]]; then
    echo "The character is a capital letter."
    else
    echo "The character is not a capital letter."
    fi
done < "$file"
final_line+="$tmp_string"
echo -e $final_line > ./output/desc.txt