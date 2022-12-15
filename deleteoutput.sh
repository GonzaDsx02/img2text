ls -la ./*[!x]txt > files.txt

while IFS="./" read -r a b c; do 
    rm "$c" ; 
done < files.txt