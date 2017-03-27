# -*- coding: utf-8 -*-
"""
Created on Mon May  4 09:47:46 2015

@author: liran
"""

class A:
    @staticmethod
    def st():
        print "static"
    def __init__(self,num):
        self.__num = num
        print "A"
    def f1(self):
        print self.__num

class B(A):
    def __init__(self,num,size):
        A.__init__(self,num)
        self.__size=size
        print "B"
        
        
#a1=A()
A.st()
B.st()

b1=B(2,3)
b1.f1()