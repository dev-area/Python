# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:33:14 2015

@author: liran
"""
def myzip(a,b):
    x1=len(a)
    y1=len(b)
    z1=min(x1,y1)
    ret=[(a[0],b[0])]
    for i in range(1,z1):
        ret += [(a[i],b[i])]
    return ret
    

print myzip("abcd","xyzw")

print myzip([3,4,5,6],[5,6,7,8])