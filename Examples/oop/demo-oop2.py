#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:59:00 2017

@author: parallels
"""

import copy
class Date:
 
    def __init__(self, day=0, month=0, year=0):
        self.__day   = day
        self.__month = month
        self.__year  = year
        
    def __str__(self):
        return str(self.__day)   + '/' + \
               str(self.__month) + '/' + \
               str(self.__year)
               
    def __add__ (self, value):
        retn = copy.deepcopy(self)
        retn.__day = retn.__day + value
        #retn.__validate_date()
        return retn


d = Date(1,2,2010)

print d
d+=1
print d

