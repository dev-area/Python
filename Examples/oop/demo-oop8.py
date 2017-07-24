#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 17:45:05 2017

@author: parallels
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 15:20:30 2017

@author: parallels
"""

class Invoker(object):
    
    def __init__(self):
        self._subscribers = []
    def __add__(self,subscriber):
        self._subscribers.append(subscriber)
        return self
    def __sub__(self,subscriber):
        if(subscriber in self._subscribers):
            self._subscribers.remove(subscriber)
        return self
    def Invoke(self,message,exclude=None):
        for s in self._subscribers:
            if(s!=exclude):
                s(message)
   

def handler1(message):
    print "handler1 got:" + message
def handler2(message):
    print "handler2 got:" + message
def handler3(message):
    print "handler3 got:" + message
def handler4(message):
    print "handler4 got:" + message
    
class A(object):
    def __init__(self,val):
        self.__val=val
    def handler5(self,message):
        print "handler1 got:" + message + " with " + str(self.__val)

inv = Invoker()

a1 = A(10)
a2 = A(20)
inv+=a1.handler5
inv+=a2.handler5
inv+=handler1
inv+=handler2
inv+=handler3
inv+=handler1
inv+=handler4
inv.Invoke("Hi all")
print
inv-=(handler1)
inv-=(handler1)

inv.Invoke("Hi all",handler1)
