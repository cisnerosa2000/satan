import os
import glob

for roots, dirs, files in os.walk("../"):
   for f in files:
       os.system("chmod u-rwx %s" % f)