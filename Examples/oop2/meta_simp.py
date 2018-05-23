#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 21:55:13 2018

@author: liran
"""

class A(type):
    def __call__(c,arg):
        print("A")

class B(object):
    def __call__(c,arg):
        print("B")

class C(B,metaclass=A):
    def __call__(c,arg):
        print("C")

c1= C(10)