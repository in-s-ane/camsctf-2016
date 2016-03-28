import hashlib

combined_hash = "13990FF50FF37CBCEDE9AB7382BBC7B6BB3B393C8C8476F4DE6ECF815CCF683E66F69229".lower()
sha1_hash = combined_hash[:40]
md5_hash = combined_hash[40:]

# Salt is in hex
salt = str(hex(8023748904807506340)[2:]).lower()

for combination in range(1000000,10000000):
    combination = str(combination)
    print combination
    md5 = hashlib.md5(combination+salt).hexdigest().lower()
    if md5 == md5_hash:
        print "Flag: {%s}" % combination
        break

# Although LG uses a seemingly different method for locking their phones, everything boils down to the same stuff as aosp.
# Knowing this, we know exactly how the password is stored:
# hash = sha1(password + salt) + md5(password + salt)

# In device_policies.xml, we find that the password is 7 digits long, and that the salt is "8023748904807506340" (lockscreen.db)
# Md5 is much faster than sha1, so let's crack that instead.
# Trying out all possible combinations reveals the correct password.

# {1143224}
