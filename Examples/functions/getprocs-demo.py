#import GetProcs

class GetProcs:
    d = [(i, i**3,str(i**2)) for i in range(10)]
    i = 0

    @classmethod
    def GetFirstProc(cls):
        #print 'GetFirstProc - {} (i={}, d={})'.format(cls.d[cls.i], cls.i, cls.d)
        cls.i = 0
        return cls.d[cls.i]

    @classmethod
    def GetNextProc(cls):
        #print 'GetNextProc - {} (i={}, d={})'.format(cls.d[cls.i], cls.i, cls.d)
        cls.i += 1
        if cls.i >= len(cls.d):
            return False
        return cls.d[cls.i]

#def iGetProcs():
#    print 'iGetProcs'
#    nextProc = GetProcs.GetFirstProc()
#    yield nextProc
#
#    while nextProc:
#        nextProc = GetProcs.GetNextProc()
#        if nextProc:
#            yield nextProc
   
###################################################################

def iGetProcs():
    
    Retn = GetProcs.GetFirstProc()
    yield Retn
    
    while Retn:
        Retn = GetProcs.GetNextProc()
        if Retn:
            yield Retn
            

###################################################################

for proc in iGetProcs():
    print(proc)
    
#pids = dict()
#for value in iGetProcs():
#    pids[value[0]] = value[1:3]
#
#print(pids)
#    
#pids = {pid:value for pid,value in iGetProcs()} 
#
#print(pids)