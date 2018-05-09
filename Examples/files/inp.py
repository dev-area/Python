import  fileinput
import sys

print(sys.argv)
 
for line in fileinput.input():
      print (fileinput.filename())
      print (line + ':' + str(fileinput.lineno()))
