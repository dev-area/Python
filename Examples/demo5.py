# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 18:02:46 2015

@author: liran
"""

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook


image_file = cbook.get_sample_data('/Users/liran/hires.png')
image = plt.imread(image_file)

plt.imshow(image)
plt.axis('off') # clear x- and y-axes
plt.show()



