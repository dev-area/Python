#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 09:14:59 2017

@author: liran
"""

class A(object):
    def __init__(self,a,b):
        self.__a = a
        self.__b = b
    def myprint(self):
        print ('a=', self.__a, 'b=', self.__b)
    def __call__(self,num):
        print ('call:', num + self.__a)
    

a1=A(10,20)
a1.myprint()

a1(80)


