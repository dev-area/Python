# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 00:02:43 2015

@author: liran
"""

def f1(x,y):
    try:
        z=x/y
        x=raw_input("enter full file name")
        y=open(x,"r")
        
        assert z<78,'ggg'
        return z
    except Exception,d:
        print 'error',d
        return 0
    except (AssertionError,IOError), dd:
        print 'aaaaa',dd
    finally:
        print 'finally'
        return 7
        

print f1(12,3)