#!/bin/bash
#input="/path/to/txt/file"
while IFS= read -r line
do
    res=$(grep ".00")
    echo "$res"
done < output1.txt
#done < "$input"