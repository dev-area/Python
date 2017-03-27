# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 22:59:09 2015

@author: liran
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb, [0.299, 0.587, 0.144, 0])

img = mpimg.imread('/Users/liran/hires.png')     
gray = rgb2gray(img)    
#gray = signal.medfilt2d(gray, [15,15])

plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.show()


