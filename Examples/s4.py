# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:42:30 2015

@author: liran
"""

def histogram(seq):
    d = dict()
    for element in seq:
        if element not in d:
            d[element] = 1
        else:
            d[element] += 1
    return d

def print_hist(hist):
    for key,val in enumerate(hist):
        print key, val

h = histogram('brontosaurus')
print h
print_hist(h)

