#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 07:59:00 2017

@author: liran
"""

num = 9

def f1():
    global num
    num=20
    
def f2():
    print num
    

f2()
f1()
f2()