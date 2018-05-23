#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 09:22:55 2018

@author: liran
"""

class A(object):
    def __init__(self):
        print('Running A.__init__')
        super(A,self).__init__()
class B(A):
    def __init__(self):
        print('Running B.__init__')   
        A.__init__(self) 

class C(A):
    def __init__(self):
        print('Running C.__init__')
        A.__init__(self);

class D(B,C):
    def __init__(self):
        print('Running D.__init__')
        B.__init__(self)
        C.__init__(self)

foo=D()