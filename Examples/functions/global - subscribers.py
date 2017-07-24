#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 09:30:44 2017

@author: parallels
"""

subscribers = []

def register(subscriber):
    global subscribers
    subscribers.append(subscriber)
def unregister(subscriber):
    global subscribers
    if(subscriber in subscribers):
        subscribers.remove(subscriber)
def invoke(message,exclude=None):
    global subscribers
    for s in subscribers:
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
    
register(handler1)
register(handler2)
register(handler3)
register(handler1)
register(handler4)
unregister(handler1)
unregister(handler1)
invoke("Hi all",handler2)
    