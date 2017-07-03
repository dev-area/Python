import sys
import mytimer
#import mymodules.mytimer2 as mytimer

mytimer.start_timer()
lines = 0
try:
    for row in open ("words"):
        lines += 1
except IOError as err: 
    print >> sys.stderr,"Could not open:", \
           err.filename, err.args[1] 
    
mytimer.end_timer()
print "Number of lines:",lines

try:
    mytimer.end_timer()
except SystemError, err:
    print >> sys.stderr,"end_timer error:",err

print "We are all done"
