enc = open("askey.txt", "r").read()

flag = ""
for char in enc:
    flag += chr(ord(char) - 13)

print flag.strip("flag") # Flag format...

# {utf-8anyone?no?fine}
