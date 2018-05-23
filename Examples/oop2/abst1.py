#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 18:50:29 2018

@author: liran
"""

class A(object):
    def __init__(self):
        raise Exception("Error")
    def f1(self):
        pass
    def f2(self):
        pass
    def f3(self):
        print("f3 A")
    
    
def templatefn(a1):
    print("======")
    a1.f1()
    a1.f2()
    a1.f3()
    print("======")
    

class B(A):
    def __init__(self):
        print("init")
    def f1(self):
        print("f1")
    def f2(self):
        print("f2")
    def f3(self):
        print("f3 B")
        A.f3(self)

a1 = B()
templatefn(a1)

