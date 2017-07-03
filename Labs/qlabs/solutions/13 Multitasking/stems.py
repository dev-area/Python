import mytimer

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
# a)   28 worker processes
# b)    2 worker processes 14 stem sizes each
# c)    2 worker processes using a queue

mytimer.start_timer()
n = 30

for stem_size in range(2,n+1):
    best_stem = ""
    best_count = 0

    for (stem,count) in stems.items():
       if stem_size == len(stem) and count > best_count:
           best_stem  = stem
           best_count = count


    if best_stem:
        print "Most popular stem of size",stem_size,"is:", \
               best_stem,"(occurs",best_count,"times)"
                
mytimer.end_timer('Process')  



