#!/usr/bin/python
# Python 2 version
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
    print  "{0:<12}: {1:01.3f} seconds".format(txt,end_time-start_time) 
        
###########################################################################
import platform
import os.path
import sys
import glob
from threading import Thread
from Queue import Queue

########################################################################

def RemoveThread(*args):
    TargetDir,queue = args
    
    while True:
        FName = queue.get()
        if not FName: break    
        os.remove(TargetDir + FName)
        

def WorkerThread(*args):
    
    TargetDir,queue,rqueue = args
    
    while True:
        
        FName = queue.get()
        if not FName: break
        
        Data = open(FName,'rb').read()
        
        FName = os.path.basename(FName)
        fh = open(TargetDir + FName,'wb')
        fh.write(Data)
        fh.close()

        #print 'Copied {} to {}'.format(FName,TargetDir) 
    
        rqueue.put(FName) 
        #os.remove(TargetDir + FName)
    
########################################################################

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
NumThreads = 2

for i in range(0,10):

    print 'Loop',i 
    queue  = Queue()
    rqueue = Queue()

    Tids = []

    for i in range(0,NumThreads):
        Tids.append(Thread(target=WorkerThread, args=(TargetDir,queue,rqueue)))
    
    rth = Thread(target=RemoveThread, args=(TargetDir,rqueue))

    for th in Tids:
        th.start()

    rth.start()
    
    for FName in glob.iglob(Source):    
        queue.put(FName) 
    
    for th in Tids:
        queue.put(False)
    
    for th in Tids:
        th.join()
    
    rqueue.put(False)
    rth.join()
    
end_timer("Threaded:")
