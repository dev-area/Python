#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 17:21:46 2017

@author: parallels
"""

fh = open('t2.txt', 'r+')

index={}
while True:
    line = fh.readline()
    if not line: break
    fields = line.split(',')
    index[fields[1].rstrip()] = fh.tell() - len(line) 
print index
key = raw_input('Enter a key:')  
fh.seek(index[key])
print fh.readline()

fh.close()
