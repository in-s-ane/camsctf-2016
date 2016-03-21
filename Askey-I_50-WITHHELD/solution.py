enc = open("askey.txt", "r").read()

flag = ""
for char in enc:
    flag += chr(ord(char) - 13)

print flag

# flag{utf-8anyone?no?fine}
