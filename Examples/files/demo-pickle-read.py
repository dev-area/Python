#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 18:21:10 2017

@author: parallels
"""


import cPickle as pickle

d = open("nums.p",'rb')
list = pickle.load(d)


print list

list = pickle.load(d)
d.close()

print list