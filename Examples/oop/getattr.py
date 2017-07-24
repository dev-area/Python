#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 17:16:07 2017

@author: liran
"""

class A(object):
    def __init__(self,a,b):
        self.a1 = a
        self.b1 = b
        print 'init'
    def mydefault(self):
        print 'default'
    def __getattr__(self,name):
        print "other fn:",name
        return self.mydefault

a1 = A(10,20)
a1.fn1()