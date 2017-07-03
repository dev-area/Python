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

for proc in iGetProcs():
    print(proc)
