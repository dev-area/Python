#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 00:19:18 2017

@author: parallels
"""
import inspect
import sys
class Account(object): 
    def __init__(self, initial):
        self._balance = initial 
    def deposit(self, amt):
        self._balance = self._balance + amt 
    def withdraw(self,amt):
        self._balance = self._balance - amt 
    def getbalance(self):
        return self._balance
    def __str__(self):
        return "Balance:" + str(self._balance)


class Checking(Account):
    def __init__(self):
        super(Checking,self).__init__(0)
        
def add(a,b):
    return a+b

c = Checking()

print isinstance (c,Account)

print Account.__dict__
#print inspect.__dict__

#print sys.modules[__name__].__dict__

a = getattr(sys.modules[__name__],'Account')
a1 = a(10)
print a1.getbalance()

a = eval('Account(90)')
if hasattr(a,'getbalance'):
    print getattr(a,'getbalance')()
    
print inspect.getsource(Account)
print inspect.getmembers(sys.modules[__name__])

f = getattr(sys.modules[__name__],'add')
print inspect.getargspec(f)


