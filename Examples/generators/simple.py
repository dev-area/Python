#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 11:42:18 2017

@author: liran
"""

def fn():
    num = 10
    for i in range(3):
        num+=1
        yield num
        
a=fn()

print a.next()
print next(a,False)
print next(a,False)
print next(a,False)

