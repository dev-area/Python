# -*- coding: utf-8 -*-


import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[12,32,23],[54,25,76],[17,78,39]])

print A+B

print A+B*3
print np.min(B)
print np.max(B)
print A.T
A=A-np.min(A)
print A
print np.invert(A)
print np.sum(A)

B = np.array([[1,2],[3,4]])
x=np.array([3,0])


print np.linalg.det(B)

print np.linalg.solve(B,x)

