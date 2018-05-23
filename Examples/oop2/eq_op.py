#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 08:06:46 2017

@author: parallels
"""

class Test(object):

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

t1 = Test("foo", 42)
t2 = Test("foo", 42)
t3 = Test("bar", 42)

print (t1, t2, t3)
print (t1 == t2)
print (t2 == t3)
print (t2 is t1)

t2 = t1;
print (t2 is t1)