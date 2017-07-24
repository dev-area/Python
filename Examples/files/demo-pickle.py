#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 18:05:51 2017

@author: parallels
"""

import pickle
list  = [1,2,3]

d = open("nums.p",'wb')
pickle.dump(list,d,pickle.HIGHEST_PROTOCOL)

list  = [10,20,30]


pickle.dump(list,d)

d.close()