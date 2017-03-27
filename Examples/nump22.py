# -*- coding: utf-8 -*-
"""
Created on Sat Jan  3 23:08:46 2015

@author: liran
"""

import numpy as np
import pylab


B = np.array([[1,2],[3,4]])
x=np.array([3,0])
print x
print np.linalg.solve(B,x)