#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 22:23:58 2017

@author: parallels
"""
def g():
    yield 1
    yield 2
    yield 3
    
gen = g()
print gen.next()
#print gen.send(4)
print gen.next()
print gen.next()
#print gen.next()

for i in g():
    print i

import glob, os

def get_dir(path):
   while True:
        pattern = path + '/*'
        
        for file in glob.iglob(pattern):
            if os.path.isdir(file):
                path = yield file  # return value is None unless send is called
                if path: 
                    break
        
        if not path: break  
            
gen = get_dir('/')
#
print next(gen) 
print next(gen)  
print gen.send('/home')
#print next(gen) 

