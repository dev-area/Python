import signal
import time

class MyError(Exception): 
    pass

def handler(sig, frame):
    raise MyError('Received signal ' + str(sig) +
                  ' on line ' + str(frame.f_lineno) +
                  ' in ' + frame.f_code.co_filename)    

signal.signal(signal.SIGINT, handler)

try:
    while 1:
        time.sleep(1)    
except KeyboardInterrupt:
    print 'Keyboard interrupt caught'
except MyError as err:
    print "Hiccup:",err
    
print 'Clean exit'

