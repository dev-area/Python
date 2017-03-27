# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 00:57:43 2015

@author: liran
"""

import numpy
import matplotlib.pyplot as plt


x = numpy.arange(50)*2*numpy.pi/50
y=numpy.sin(x)

fig, ax = plt.subplots()


plt.plot(x,y, '-o', picker=4)  


def on_pick(event):
    thisline = event.artist
    xdata, ydata = thisline.get_data()
    ind = event.ind
    ax.cla()
    ax.text(5,0,str(xdata[ind]),fontsize=15)
    plt.plot(x,y, '-o', picker=4) 

cid = fig.canvas.mpl_connect('pick_event', on_pick)
