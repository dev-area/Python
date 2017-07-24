#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 20:48:31 2017

@author: parallels
"""



def add(a,b):
    if(a<0):
        # 2 args, first is Exception, second is message 
        raise Exception,2
    return a+b


try:
    print add(-2,3)
except ValueError as a:
    print a
except:
    print "def"
    raise

def add(a,b):
    if(a<0):
        raise Exception("negative")
    return a+b


try:
    print add(-2,3)
except Exception,b:
    print b