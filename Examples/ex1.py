# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 22:54:34 2015

@author: liran
"""

import numpy as np
import pylab as py

x=np.loadtxt('/users/liran/data1.txt')

print x[0]
py.plot(x[1],x[0],'g-s')
lb=['aa','bb','cc','ff','gg','jj','kk','uu']
p,s=py.pie(x[1])
py.legend(p,lb)
