#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 09:12:52 2017

@author: parallels
"""
import re
def countuppers(st):
    return len(re.findall(r'[A-Z]',st))

def countlowers(st):
    return len(re.findall(r'[A-Z]',st))


   
     