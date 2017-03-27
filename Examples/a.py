# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:10:17 2015

@author: liran
"""
from pydoc import help #jhggjg
h=90
'''
def fn(x):
    """return msg.
    x -- real part
    
    """
    h=80
    
    print "hello",h , global h
''' 
"""
def mulby(num):
    def gn(val):
        return num*val
    return gn
    
zw=mulby(7)
print( zw(9));


    
def fn(x):
    def gn(y):
        return y*x
    return gn    

x1=fn(10)
print x1(20)


def keep(low,high):
    def ch(num):
        if num < low:
            return low
        elif num > high:
            return high
        else:
            return num;
    return ch
    
v1=keep(45,67)
print v1(55)
"""


def genfilterby(mod):
    def gn1(lst):
        x=[]
        for i in lst:
            if i % mod == 0:
                x+=[i]
        return x
    return gn1
        
fil=genfilterby(3)
z=[2,3,4,5,6,7,8] #hjhkjh


print( fil(z));
"""
#print fn.__doc__
#print help(fn)
"""
