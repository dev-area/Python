# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def testfn(f,x,y):
    return f(x) + y
    
def add10(c):
    return c+10
    

print testfn(add10,3,5)

'''
import numpy as np
from pylab import *

a = np.array([1, 4, 5, 8], float)
b = np.array([1, 2, 3, 4], float)
a=a*b

print(a[1])
plot(a,b)


from numpy import *
import pylab as pl
t = linspace(0,2*pi,400)
x = array([cos(t),sin(t)])
A  = array([[1.,1.],[1.1,1]])
Ax = dot(A,x)
Ainv  = linalg.inv(A)
Ainvx = dot(Ainv,x)
pl.subplot(1,2,1,aspect='equal')
pl.plot(  x[0,:],  x[1,:], 'b' )
pl.plot( Ainvx[0,:], Ainvx[1,:], 'r' )
pl.subplot(1,2,2,aspect='equal')
pl.plot(     x[0,:],     x[1,:], 'b' )
pl.plot( Ax[0,:], Ax[1,:], 'r' )
pl.show()

'''
