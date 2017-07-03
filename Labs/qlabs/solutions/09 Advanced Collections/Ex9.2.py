import GetProcs

   
###################################################################

def iGetProcs():
    
    Retn = GetProcs.GetFirstProc()
    yield Retn
    
    while Retn:
        Retn = GetProcs.GetNextProc()
        if Retn:
            yield Retn

###################################################################
pids = dict()
for value in iGetProcs():
    pids[value[0]] = value[1:3]

print(pids)
       