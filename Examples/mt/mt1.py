import multiprocessing
def fn(a,b):
    print ("vals=",a,b)

proc1 = multiprocessing.Process(target=fn, args=(10,20))
proc2 = multiprocessing.Process(target=fn, args=(30,50))
proc1.start()
proc2.start()
proc1.join()
proc2.join()
