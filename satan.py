import os
def is_ascii(s):
    return all(ord(c) < 128 for c in s)
for roots, dirs, files in os.walk("/"):
   for f in files:
      filename = f if is_ascii(f) else "unicode"
      print filename