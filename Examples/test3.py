# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 13:05:17 2014

@author: liran
"""

class A(object):
    def __init__(self,a):
        self.__a = a
        print "Constructor A was called"
    def Print(self):
        print("val=" + str(self.__a))

class B(object):
    def __init__(self,b):
        self.__innerA = A(b+10)
        print "Constructor B was called"
    def fn(self):
        print("B fn")
        self.__innerA.Print()

class Point:
    pass

p1=Point()
p1.x =10
p1.y = 20

print('(%g, %g)' % (p1.x, p1.y))

b = B(100)
b.fn()





