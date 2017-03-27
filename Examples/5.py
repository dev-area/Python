# -*- coding: utf-8 -*-



import numpy as np
import pylab

def plot(f,a,b,num_points):
    # Shows the plot of function f between a and b, 
    # taking num_points point equispaced
    x = np.linspace(a,b,num_points)
    y = f(x)
    pylab.plot(x,y)

def my_function(x):
    my_result = x*np.cos(1/x)
    return my_result


plot(my_function,0,np.pi/4,1000)
pylab.show()
