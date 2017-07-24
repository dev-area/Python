#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:53:08 2017

@author: parallels
"""

compare=lambda a,b: -1 if a < b else (1 if a > b else 0)

x = 42
y = 3

print "a>b",compare(x,y)


def make_grthan(n):
    return lambda m: False if n>m else True

grthan3 = make_grthan(3)

print grthan3(2)