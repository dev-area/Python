# -*- coding: utf-8 -*-


import numpy as np

def scale(A):
    A[-1, :] *= 2
    A[:, -1] *= 2
    
M = np.array([[1, 2], [3, 4]])
scale(M)
print M