#!/usr/bin/python
import sys, fileinput, re, glob

print sys.argv.count

pattern = sys.argv.pop(1)

#sys.argv[1:] = glob.glob(sys.argv[1])

more_files = len(sys.argv[1:])

for line in fileinput.input():
   m = re.search(pattern, line)
   if m:
      if more_files > 1:
         print fileinput.filename()
      print line + ':' + str(fileinput.lineno())
