import os
def is_ascii(s):
    return all(ord(c) < 128 for c in s)
for i in xrange(0x3E8):
    os.system("touch documents/%s.txt") % i
