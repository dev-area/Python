#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 12:04:21 2017

@author: parallels
"""


def dup_strg(val, times):    
   global res
   res = str(val) * times 
   return res

def dup_str(val, times):    
   res = str(val) * times 
   return res

def print_vat(gross, vatpc=17.5, message='Summary:'):
   #print print_vat.func_defaults
   net = gross/(1 + (vatpc/100))
   vat = gross - net
   print message,'Net: %5.2f' % net, 'Vat: %5.2f' % vat
print_vat(9.55,message="ss")

def myfunc(dir, *files):
    print "dir:", dir, "files:", files 

def sayhello(a):
    """ sayhello gets a string parameter a 
        and prints 'hello ' a.
    """
    print 'hello ' + a
    
myfunc('c:/stuff', 'f1.txt', 'f2.txt', 'f3.txt')

t = ('myfolder','b','c')
myfunc(*t)
print help(sayhello)
#
#
def print_vat (**kwargs):
   print kwargs

print_vat(vatpc=15, gross=9.55, message='Summary')

Argsdict = dict(vatpc=15, gross=9.55, message='Summary')
print Argsdict
print_vat(**Argsdict)

Argsdict = {'vatpc':15,'gross':9.55,'message':'sum'}
print_vat(**Argsdict)

result = 3

def generic_form(*args,**kwargs):
    print args
    print kwargs

generic_form(1,2,3,a=4,b=5)

def scope_test1(): 
   #global result
   result = 42

scope_test1()
print result

def scope_test2():    
   global result
   result += 2

scope_test2()
print result

def outer():
    num = 42

    def inner():
        print num, "in inner"
        
    inner()
    print num, "in outer"
    
outer()
#inner()
