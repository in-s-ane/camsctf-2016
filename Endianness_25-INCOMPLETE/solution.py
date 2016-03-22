# $ hexdump rev
# 0000000 de42 92e2 fa2c 7626 fa36 962e 2e36 a6fa
# 0000010 cc76 268c 2c76 be00                    
# 0000018
# $ hexdump endian.txt
# 0000000 42de e292 2cfa 2676 36fa 2e96 362e faa6
# 0000010 76cc 8c26 762c 00be                    
# 0000017

# welp i reversed the endianness but it ain't workin?

s = "\xde\x42\x92\xe2\xfa\x2c\x76\x26\xfa\x36\x96\x2e\x2e\x36\xa6\xfa\xcc\x76\x26\x8c\x2c\x76\xbe\x00"

print s
a =  "".join("".join(i) for i in zip(s[1::2], s[::2]))
print a

f = open("rev", 'w')
f.write(a)
f.close()

