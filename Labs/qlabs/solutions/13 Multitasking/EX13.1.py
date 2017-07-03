from subprocess import *
import os
import sys

#(a)
proc = Popen([sys.executable, 'client.py', 'words']) 
proc.wait()
print "Child exited with",proc.returncode

#(b)
proc = Popen([sys.executable, 'client.py', 'words'],
             stdout=PIPE, stderr=PIPE)
(output, error) = proc.communicate()

if error != None:
    print "error:", error
    
print "output:", output


