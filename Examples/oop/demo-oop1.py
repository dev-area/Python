#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:24:10 2017

@author: parallels
"""

class Account: 
    numCreated = 0
    def __init__(self, initial):
        self.__balance = initial 
        self.list = [1,2,3]
        Account.numCreated += 1
        self.__name="Avi"
    def deposit(self, amt):
        self.__balance = self.__balance + amt 
        self.list+=[self.__balance]
    def withdraw(self,amt):
        self.__balance = self.__balance - amt 
    def getbalance(s):
        return s.__balance
    def getlist(self):
        return self.list
    def __str__(self):
        return "bal:" + str(self.__balance)
    @property 
    def owner(self):
        return self.__name
    @owner.setter
    def owner(self,value):
        self.__name = value
   
#    @owner.deleter
#    def owner(self):
#        print "del"
#        self.__name = None
#    @classmethod
#    def shownum(cls):
#        cls.aaa=20
#        print cls.numCreated
#    @classmethod
#    def shownum3(cls):
#        return cls.aaa
#    @staticmethod
#    def shownum2():
#        print Account.numCreated
    
    
a = Account(9)
Account.numCreated +=1
print Account.numCreated
print a

#del a.owner

print a.owner
a.deposit(10000)
#Account.shownum()
