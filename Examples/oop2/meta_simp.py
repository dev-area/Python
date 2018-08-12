#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 21:55:13 2018

@author: liran
"""

class A(type):
    def __call__(c,arg):
        c.xyz=900
        print("A",arg)
        return super(A,c).__call__(arg)

class B(object):
    def __call__(c,arg):
        print("B")
    def fn(self):
        print("B fn")

class C(B,metaclass=A):
    def __call__(c,arg):
        print("C")
    def __init__(self,x):
        print("C init",x)
    def pr(self):
        print

     

c1= C(10)






def cldec(ccls):
     class Inner(ccls):
         attr = 1008
     return Inner

@cldec
class X:
    def f1(self,v1):
        print("f1")
        self.v=v1
    def f2(self):
        print(self.v)


