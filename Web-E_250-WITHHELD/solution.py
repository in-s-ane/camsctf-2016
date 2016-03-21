from z3 import *

s = Solver()
s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18 = BitVecs('s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18', 32)

s.add(s0 >= 32)
s.add(s1 >= 32)
s.add(s2 >= 32)
s.add(s3 >= 32)
s.add(s4 >= 32)
s.add(s5 >= 32)
s.add(s6 >= 32)
s.add(s7 >= 32)
s.add(s8 >= 32)
s.add(s9 >= 32)
s.add(s10 >= 32)
s.add(s11 >= 32)
s.add(s12 >= 32)
s.add(s13 >= 32)
s.add(s14 >= 32)
s.add(s15 >= 32)
s.add(s16 >= 32)
s.add(s17 >= 32)
s.add(s18 >= 32)

s.add(s0 <= 126)
s.add(s1 <= 126)
s.add(s2 <= 126)
s.add(s3 <= 126)
s.add(s4 <= 126)
s.add(s5 <= 126)
s.add(s6 <= 126)
s.add(s7 <= 126)
s.add(s8 <= 126)
s.add(s9 <= 126)
s.add(s10 <= 126)
s.add(s11 <= 126)
s.add(s12 <= 126)
s.add(s13 <= 126)
s.add(s14 <= 126)
s.add(s15 <= 126)
s.add(s16 <= 126)
s.add(s17 <= 126)
s.add(s18 <= 126)

s.add(s6 == s12)
s.add(s10 == 95)
s.add((s3 - s5) == (s17 - s11) * 9)
s.add(s5 + s11 + s17 == 293)
s.add(s17 - s11 + s5 == 69)
s.add(s3 == (s18 - 15))
s.add(s18 == 100) # derived from above
s.add(s0 == s16)
s.add(s9 == s18)
s.add((s0 & s6) == (s0 - 16))
s.add((s2 | s4) == s15)
s.add((s6 >> 1) == (s0 << 1)/2.0)
s.add((s4 & s6) == s12)
s.add((s10 ^ s4) == 44)
s.add(s4 == s13)
s.add((s16 | 1) == s16 + 1)
s.add((s13 - 32) == s14)
s.add((s13 >> 5) * 34 == s2)
s.add((((s1 % 7) + 3) | s16) == s8)
s.add((s2 + s1) / 2 == s18)
s.add(s18 % 10 == 0)
s.add(s8 == s2 / 2)

l = [0] * 19

s.check()
m = s.model()
for x in m:
    l[int(str(x)[1:-1])] = m[x]

l[18] = 100

for x in l:
    print x

# so this gives us most of the password.
# guess the rest to get the real password:
# 0bfUsCat3d_pasSw0rd

# {why_lujing_why_w0uld_you_do_this}
