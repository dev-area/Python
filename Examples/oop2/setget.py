#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 13:55:07 2017

@author: liran
"""

class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        print ('get')
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        print ('set')
        self._x = value

    @x.deleter
    def x(self):
        print('del')
        del self._x
        

c1=C()

print (c1.x)
c1.x = 10;
print (c1.x)
del (c1.x)
c1.y=70
print (c1.y)

#print (c1.x)



