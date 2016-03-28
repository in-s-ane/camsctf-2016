key = 66

enc = open("repeat1.txt", "r").read().strip().decode("hex")

dec = ""

for char in enc:
    dec += chr(ord(char) ^ key)

print dec

# Checking out the difference between the first char and "{", as well as the last char and "}"
# revealed that the key was probably 66.

# Since plaintext ^ key ^ key = plaintext, we can reverse the xor

# {x0r_xor_XOR_XOR}
