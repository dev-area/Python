#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 08:58:52 2017

@author: liran
"""

ls = [1,2,3,4]
ls2 = [i for i in ls if i>2]
print ls2
ls2 = [i*2 for i in ls if i>2]
print ls2
d1 = {x: x**2 for x in (2, 4, 6)}
print d1
d1 = {x: 'item' + str(x**2) for x in (2, 4, 6)}
print d1
a = {x for x in 'abracadabra' if x not in 'abc'}
print a