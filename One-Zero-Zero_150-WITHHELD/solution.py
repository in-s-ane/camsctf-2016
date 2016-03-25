def decrypt_RSA(privkey, message):
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    from base64 import b64decode
    key = open(privkey, "r").read()
    rsakey = RSA.importKey(key)
    decrypted = rsakey.decrypt(message)
    return decrypted

dec = ""

for x in range(1, 17):
    enc = open("%s.enc" % x, "r").read()
    dec += decrypt_RSA('priv.key', enc)

print dec

# Running openssl rsa -in key.pub -pubin -text -modulus gives us our modulus:
# 2C8D59AF47C81AB3725B472BE417E3BF7AB85439AF726ED3DFDF66489D155DC0B771C7A50EF7C5E58FB
# python -c "print int('2C8D59AF47C81AB3725B472BE417E3BF7AB85439AF726ED3DFDF66489D155DC0B771C7A50EF7C5E58FB', 16)"

# Now that we have N, we can factor it out to get p and q.
# http://factordb.com/index.php?query=1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139

# Now that we know p and q, we can plug them into rsatool and generate the private key.

# $ python rsatool.py -p 37975227936943673922808872755445627854565536638199 -q 40094690950920881030683735292761468389214899724061 -o priv.key

# Now that we have the private key, we can decrypt the chunks and get the flag.

# $ python solution.py

# Dear Lora Sum,
# Hello, Lora
# Remember to attack at 6:00 AM
# I've encrypted the message just in case
# I mean,
# flag{it'sc4lledpriv4tefor4re4son}
# Sincerely,
# Brad Turk

# {it'sc4lledpriv4tefor4re4son}
