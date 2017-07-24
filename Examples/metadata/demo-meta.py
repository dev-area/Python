#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 10:42:27 2017

@author: parallels
"""

import os
import inspect
print os.name


class Account(object): 
    numCreated = 0
    def __init__(self, initial):
        self.__balance = initial 
        self.list = [1,2,3]
       
        Account.numCreated += 1
    def deposit(self, amt):
        self.__balance = self.__balance + amt 
        self.list+=[self.__balance]
        return self.__balance
        
    def withdraw(self,amt):
        self.__balance = self.__balance - amt 
    def getbalance(s):
        return s.__balance
    def getlist(self):
        return self.list
    def __getattr__(self, aname):
        return lambda x:x+2
    def __delattr__(self, aname):
        pass

class Checking(Account):
    def __init__(self):
          #super(Checking,self).__init__(0)
          Account.__init__(self,0)
    def deposit(self, amt):
         print "ceck"
         Account.deposit(self,amt)

class Proxy:
    def __init__(self, obj):
        self._wrapped = obj          
    
    def __getattr__(self, aname):
        return getattr(self._wrapped, aname)
        
#    def deposit(self, amt):
#        pass

def add(a,b):
    print a+b
#print Account.__dict__
a = Account(100)
print a.deposi(40)
c = Checking()
p = Proxy(a)
print 'proxy: ' + str(p.deposit(10))

#Account.__dict__['numCreated']=3

#delattr(Account,'withdraw')

#print inspect.getmembers(os)
m = os.__getattribute__('getegid')
m = os.__dict__['getegid']
m =getattr(os,'getegid')
setattr(os,'plus2',lambda x:x+2)

print m()
os.__dict__['pluss'] = lambda x: x+2
#os.__setattr__(plus2,lambda x: x+2)
#print m()

#print os.__dict__

#print globals()