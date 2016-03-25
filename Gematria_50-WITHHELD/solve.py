a = 46327402297733105104468896449452312521697635735182434903808055110726686224509

b = hex(a)[2:-1]
c = [b[i:i+2] for i in range(0,len(b), 2)]
d = "".join([chr(int(x,16)) for x in c])

print d.strip("flag")

# {1_b3t_"y0u"_b3c0m3s_a_z3r0}
