#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 07:48:50 2017

@author: liran
"""

class A(object):
    def __enter__(self):
        print 'enter'
    def __exit__(self,exceptType, value, traceback):
        print 'exit', exceptType

#a1 = A()
with A() as a2:
    pass

