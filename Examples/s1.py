# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:40:12 2015

@author: liran
"""
def fn(a,b):
    a1=a % 10
    b1=b % 10
    if a1>b1:
        return 1
    elif a1<b1:
        return -1
    else:
        return 0


x=[22,41,65,23,89,20,34]

x.sort(fn)
print x
