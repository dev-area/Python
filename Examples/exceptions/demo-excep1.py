#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 08:31:44 2017

@author: parallels
"""

import warnings

def fn(a):
    s=0;
    if a>100:
	       warnings.warn('Long Wait...')
    for i in range(a):
        s+=i
    return s

print "Start..."


#warnings.simplefilter('default')
#warnings.filterwarnings('error','.*')

print(fn(1000))

print "Ending..."
