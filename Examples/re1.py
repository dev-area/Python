# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:10:01 2015

@author: liran
"""
import re
x="[a-z]*@[a-z]*.[a-z]*"

s=raw_input("enter:")

c=re.match(x,s)
if c:
    print 'ok'
else:
    print 'no'    




    