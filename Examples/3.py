# -*- coding: utf-8 -*-



import numpy as np


v = np.arange(1,5)
v.shape = (4,1)
t = np.cos(np.arange(1,4))
t.shape = (1,3)
m = np.dot(v,t)
print m