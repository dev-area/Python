import sys, glob, os, stat

if sys.platform == 'win32':
    dir = os.environ['HOMEPATH']
else:
    dir = os.environ['HOME']

import re
for filename in glob.glob(dir + r'\*'):
   size = os.stat(filename)[stat.ST_SIZE]
   
   if size > 0:
      filename = re.sub(r'.*\\', '', filename)
      print filename, size, 'bytes'

print  
dirlen = len(dir) + 1
for filename in glob.glob(dir + r'\*'):
   size = os.stat(filename)[stat.ST_SIZE]
   
   if size > 0:
      print filename[dirlen:], size, 'bytes'

print
for filename in glob.glob(dir + r'\*'):
   size = os.stat(filename)[stat.ST_SIZE]
   
   if size > 0:
      print os.path.basename(filename), size, 'bytes'


