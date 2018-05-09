import  fileinput
 
for line in fileinput.input():
      print (fileinput.filename())
      print (line + ':' + str(fileinput.lineno()))
