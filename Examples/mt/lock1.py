import threading
import time

lc = threading.Lock()


def myfunc1(*args):
    global lc
    lc.acquire()
    print("From thread", args)
    lc.release()

def myfunc2(*args):
    global lc
    lc.acquire()
    print("From thread", args)
    lc.release()


tid1 = threading.Thread(target=myfunc1, args='T1')
tid2 = threading.Thread(target=myfunc2, args='T2')
tid1.start()
tid2.start()
print("From main")
tid1.join()
tid2.join()
