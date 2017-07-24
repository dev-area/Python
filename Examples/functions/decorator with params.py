#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:07:02 2017

@author: parallels
"""

def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer


@parametrized  
def my_decorator(some_function,num):

    def wrapper():

        if num == 10:
            print("Yes!")
        else:
            print("No!")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper

@my_decorator(10)
def just_some_function():
    print("Wheee!")

#just_some_function = my_decorator(just_some_function,9)

just_some_function()

