#!/usr/local/bin/python
"""
    Setup requirements:
    
    The instructor machine should be visible as INSTRUCTOR,
    and must have a directory called 'Shared', which is shareable
    
    The Linux VM must be able to see this as a share, called \\INSTRUCTOR
"""
import os

########################################################
# TIMER FUNCTIONS
start_time = 0;

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
    print "{0:<12}: {1:01.3f} seconds".format(txt,end_time-start_time)
        
###########################################################################
import platform
import os.path
import glob
import sys

OperSys,Host = platform.uname()[:2]
Source = './Bitmaps'

if not os.path.isdir(Source):
    sys.exit("Unable to access "+Source)

Source = Source + '/*'


if OperSys == 'Windows':
    TargetDir = '\\\\INSTRUCTOR\\Shared\\' + Host + '\\'
    #TargetDir = '\\\\BUTTON\\Shared\\' + Host + '\\'
else:
    TargetDir = '/mnt/hgfs/\\\\INSTRUCTOR/' + Host + '/'
   
if not os.path.isdir(TargetDir):
    os.mkdir(TargetDir)

start_timer()    

for i in range(0,10):
    
    print 'Loop',i
    Files = []
    
    for FName in glob.iglob(Source):
        Data = open(FName,'rb').read()
        
        FName = os.path.basename(FName)
        fh = open(TargetDir + FName,'wb')
        fh.write(Data)
        fh.close()
        
        Files.append(TargetDir + FName)
        #print('Copied {} to {}'.format(FName,TargetDir))
    
    [os.remove(FName) for FName in Files] 

    
end_timer("Non-threaded")
