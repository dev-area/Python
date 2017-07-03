import os
start_time = 0;

########################################################
# TIMER FUNCTIONS
def start_timer():
    """
    The start_timer() function marks the start of 
    a timed interval, to be completed by end_timer().
    This function requires no parameters.
    """
    global start_time
    (utime,stime) = os.times()[0:2]
    start_time = utime+stime

def end_timer(txt='End time'):
    """
    The end_timer() function completes a timed interval
    started by start_timer.  It prints an optional text
    message (default 'End time') followed by the CPU time
    used in seconds.
    This function has one optional parameter, the text to 
    be displayed.
    """
    (utime,stime) = os.times()[0:2]
    end_time = utime+stime
    print "%-12s: %05.3f seconds" % \
          (txt,end_time-start_time)

start_timer()
lines = 0
for row in open ("words"):
    lines += 1
    
end_timer()
print "Number of lines:",lines