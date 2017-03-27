# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:40:35 2015

@author: liran
"""

def fn(r,*arg):
    for i in arg:
        print i
 



fn(1,2,3)

def add(a,b):
    return a+b

def mul(a,b):
    return a*b
    
def div(a,b):
    return a/b
    
def sub(a,b):
    return a-b

fns=[add,sub,mul,div]

ops=[(2,4),(5,6),(7,8),(9,4)]

zi=zip(fns,ops)

print zi

print zi[0][0](zi[0][1][0],zi[0][1][1])

s = 'abc'
t = [0, 1, 2]
z = zip(s, t)
print z[0]
