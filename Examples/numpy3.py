# -*- coding: utf-8 -*-
"""
Created on Fri Dec 26 10:55:23 2014

@author: liran
"""

import numpy as np
from pylab import *

a = np.array([[0, 4, 5, 8, 10, 12],
              [1, 4, 5, 8, 10, 12],
              [1, 4, 5, 8, 10, 12],
              [1, 4, 5, 8, 10, 12],
              [1, 4, 5, 8, 10, 12],
              [1, 4, 5, 8, 10, 12]],'i8')
              
b = a.view('i4')

d=[hex(val.item()) for val in b.flat]


print(d)

dt = np.dtype("i4,f8,a5")
print dt.fields
a =np.array([(1,2.0,"Hello"), (2,3.0,"World")], dtype=dt)
print a['f2']


aa = array((0,10,20,30))
bb = array((0,1,2))
y = aa[:, None] + bb

print(y)