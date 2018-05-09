import threading
import time

class MyThread (threading.Thread):
    def run (self):
        for i in range(5):
            print ("In thread", self.name)
            time.sleep(2)

th1 = MyThread()
th2 = MyThread()
th1.setName("t1")
th2.setName("t2")
th1.start()
th2.start()
print ("From main")
th1.join()
th2.join()
