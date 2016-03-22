#!/bin/bash

if [[ $1 ]]; then
    curl http://web.camsctf.com/12/read.php -b "data=$1"
fi
