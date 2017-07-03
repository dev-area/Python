#!/usr/local/bin/python

def myfunc1(val, lista = []):
    lista.append(val)
    print "value of lista is:",lista 
    
myfunc1(42)
myfunc1(37)
myfunc1(99)


def myfunc2(val, lista = None):
    if lista == None: lista = []
    
    lista.append(val)
    print "value of lista is:",lista    
    
myfunc2(42)
myfunc2(37)
myfunc2(99)

