import signal
import time
num = 0;
 
def handler(sig, frame):
    global num
    print("CTRL+C Num=",num)
 
 
signal.signal(signal.SIGUSR1, handler)
 
while 1:
     num+=1;
     time.sleep(1)
