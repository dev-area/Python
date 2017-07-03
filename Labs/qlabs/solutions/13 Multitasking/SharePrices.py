#!/usr/local/bin/python

from threading import Thread
from threading import Lock
import time
import random

SharePrices = {'Global Motors'   :['0',50],
               'Big Blue Inc.'   :['0',50],
               'Gates Software'  :['0',50],
               'Banana Computers':['0',50]}

csSharePrices = Lock()

#########################################################################

def SetStockPrices(seq):
    # Updates stock prices with random price changes
    global SharePrices
    
    while True:
        csSharePrices.acquire()    # TODO
        for key,sp in SharePrices.items():
            SharePrices[key][0] = seq
            SharePrices[key][1] = max(1.0,
                                  sp[1] * ( 1 + ((random.random() - 0.5)/0.5) * 0.05))
            
        csSharePrices.release()    # TODO

#########################################################################

def ReadStockPrices():
    
    global SharePrices
    
    while True:
            
        csSharePrices.acquire()    # TODO
        for key,sp in SharePrices.items():
            print("{} {:<18s} ${:05.2f}".format(sp[0],key,sp[1]))
        print

        csSharePrices.release()    # TODO
        time.sleep(2)    

#####################################################################

if __name__ == '__main__':
        
    tids = []
    
    # start share price update thread
    for i in range(0,4):     
        th_set = Thread(target=SetStockPrices,args=str(i))
        th_set.start()
    
    # Wait for request from client
    for i in range(0,4):        
        
        th_st = Thread( target=ReadStockPrices )
        th_st.start()
        tids.append(th_st)
 
    for tid in tids:
        tid.join()
