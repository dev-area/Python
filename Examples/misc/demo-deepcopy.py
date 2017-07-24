#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 22:27:07 2017

@author: parallels
"""

import copy

fruit = ['knife','plate',['Apple', 'Pear', 'Orange']]
lunch = copy.deepcopy(fruit)
lunch[2][1] = 'Eggs'
print 'fruit:',fruit,'\nlunch:',lunch 
