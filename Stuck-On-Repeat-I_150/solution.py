key = 66
enc = open("repeat1.txt", "r").read().strip().decode("hex")

print "".join([chr(ord(char) ^ key) for char in enc])

# Looking at the description for Stuck On Repeat II, as well as the problem name
# seemed to suggest that the ciphertext was encrypted using xor.

# Trying to xor the first char and "{", as well as the last char and "}"
# revealed that the key was probably 66.

# Since plaintext ^ key ^ key = plaintext, we can reverse the xor

# {x0r_xor_XOR_XOR}
