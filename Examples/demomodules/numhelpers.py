#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 09:40:24 2017

@author: parallels
"""

def isdigit(c):
    return  c.isdigit()

def countdigit(st):
    return len([c for c in st if c.isdigit()]) 


def sumposnums(nums):
    return reduce(lambda x,y:x+y if y>=0 and x>=0 
                  else 0 if x<0 and y<0 else y if x<0 else x,nums)


    
    


