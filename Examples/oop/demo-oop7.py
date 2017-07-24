#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 15:20:30 2017

@author: parallels
"""

class Invoker(object):
    
    def __init__(self):
        self._subscribers = []
    def Register(self,subscriber):
        self._subscribers.append(subscriber)
    def Unregister(self,subscriber):
        if(subscriber in self._subscribers):
            self._subscribers.remove(subscriber)
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

inv = Invoker()

inv.Register(handler1)
inv.Register(handler2)
inv.Register(handler3)
inv.Register(handler1)
inv.Register(handler4)

inv.Invoke("Hi all")
    
inv.Unregister(handler1)
inv.Unregister(handler1)
inv.Invoke("Hi all",handler2)