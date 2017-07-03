import mytimer
from multiprocessing import Process, Queue
# (c)
#############################################################
def stem_search(stems, queue):

    stem_size = 1
    
    while stem_size > 0: 
        stem_size = queue.get()

        best_stem = ""
        best_count = 0

        for (stem,count) in stems.items():
            if stem_size == len(stem) and count > best_count:
                best_stem  = stem
                best_count = count

        if best_stem:
            print "Most popular stem of size",stem_size,"is:", \
                   best_stem,"(occurs",best_count,"times)"

#############################################################
if __name__ == '__main__':   

    mytimer.start_timer()

    stems = {}

    for row in open ("words"):
        for count in range(1,len(row)):
            stem = row[0:count]
            if stem in stems:
                stems[stem] += 1
            else:
                stems[stem] = 1
            #print "stem:",stem,"value:<",stems[stem],">"
       
    mytimer.end_timer('Load')        

    # Process the stems
    # Senarios:
    # a)   n worker processes
    # b)    2 worker processes n/2 stem sizes each
    # c)    2 worker processes using a queue

    mytimer.start_timer()
    n = 30
    queue = Queue()
    #for stem_size in range(2,n+1): 
    
    proc1 = Process(target=stem_search, args=(stems,queue))
    proc2 = Process(target=stem_search, args=(stems,queue))
    proc1.start()
    proc2.start()
        
    for stem_size in range(2,n):
        queue.put(stem_size)
        
    queue.put(0)
    queue.put(0)
        
    proc1.join()
    proc2.join()
                 
    mytimer.end_timer('Process')  

# Single CPU timings
#    Process     : 1.953 seconds
# a) Process     : 111.250 seconds
# b) Process     : 7.594 seconds
# c) Process     : 7.656 seconds
