#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 14:45:12 2017

@author: parallels
"""

def my_decorator(some_function):
    def wrapper():
        print("Something is happening before some_function() is called.")
        some_function()
        print("Something is happening after some_function() is called.")
    return wrapper

@my_decorator
def just_some_function():
    print("Wheee!")

#just_some_function = my_decorator(just_some_function)
just_some_function()

#########################################################################
'''
def my_decorator(some_function):

    def wrapper(num):

        if num == 10:
            print("Yes!")
        else:
            print("No!")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper

@my_decorator
def just_some_function():
    print("Wheee!")

#just_some_function = my_decorator(just_some_function,9)

just_some_function(10)


################################################################
'''