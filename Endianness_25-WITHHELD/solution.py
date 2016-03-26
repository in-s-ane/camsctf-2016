enc = open("endian.txt", "r").read().strip()
bits = ""
for byte in enc:
    tmp = ord(byte)
    bits += "{0:08b}".format(tmp)[::-1]

n = int(bits, 2)
flag = ("%x" % n).decode("hex")
print flag

# The problem name seems to suggest that we need to reverse the endian encoding, but to get the flag, we need to
# reverse all the bits in each byte.

# {BIG_4nd_little_3nd14n}
