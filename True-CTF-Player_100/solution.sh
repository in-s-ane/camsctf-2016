#!/bin/bash

expected='\\n\\t\\t<p> Are you a true CTF player?</p>\\n\\t\\t<p>Hint: Computers can stay up all night.</p>\\n\\t\\t"'

while :; do
    response=$(curl http://play.camsctf.com/api/challenges/get_challenge/\?id\=42 -b cookies.txt -s)
    if  ! echo "$response" | grep "$expected" > /dev/null; then
        echo $expected
        echo $response
        notify-send "True CTF Player" "Got the flag!" --urgency=critical
        exit 0
    else
        echo "[$(date '+%I:%M')] Received $response"
    fi
    sleep 15m
done

# Just like last year, there is a one hour time frame where the flag becomes
# visible in the problem's description really early in the morning.

# This script will request the problem description in 15 minute intervals.

# {"description": "\n\t\t<p>Flag: {0ne...m0re...ch4llenge}</p>\n\t\t", "solves": 4}
# {0ne...m0re...ch4llenge}
