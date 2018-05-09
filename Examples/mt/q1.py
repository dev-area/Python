import multiprocessing
import time

def fn1(q):
    while True:
        x=q.get()
        print ("val=",x)

def fn2(q):
    while True:
        time.sleep(2)
        q.put("hello")

queue = multiprocessing.Queue()
proc1 = multiprocessing.Process(target=fn1, args=(queue,))
proc2 = multiprocessing.Process(target=fn2, args=(queue,))
proc1.start()
proc2.start()
