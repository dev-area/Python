#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:49:31 2017

@author: parallels
"""
#
#class First(object):
#    def __init__(self):
#        print "first"
#    def ff1(self):
#        return 1
#
#class Second(First):
#    def __init__(self):
#        super(First, self).__init__()
#        print "second"
#    def ff1(self):
#        return 2
#
#class Third(First):
#    def __init__(self):
#        super(First, self).__init__()
#        print "third"
#    def ff1(self):
#        return 3
#

##########################################
#  super instead of className to call all classes when mulitple inheritance
#
############################################### 

class First(object):
  def __init__(self):
    super(First, self).__init__()
    print ("first")

class Second(object):
  def __init__(self):
    super(Second, self).__init__()
    print ("second")

class Third(First, Second):
  def __init__(self):
    super(Third, self).__init__()
    print ("that's it")      
    

f = Third()


class A(object):
    def __init__(self):
        print('Running A.__init__')
        super(A,self).__init__()
class B(A):
    def __init__(self):
        print('Running B.__init__')   
        ############################## C is not called !!! -> commen out for fix
        super(B,self).__init__()
        ########################################
        #A.__init__(self) 

class C(A):
    def __init__(self):
        print('Running C.__init__')
        super(C,self).__init__()
        #A.__init__(self);
class D(B,C):
    def __init__(self):
        print('Running D.__init__')
        super(D,self).__init__()
       # B.__init__(self)
       # C.__init__(self)

foo=D()



