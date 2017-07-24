#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 09:40:24 2017
This message will seen insdie the description 
part of the help doc
@author: parallels

"""

glbnum=9

def _isdigit(c):
   
    return  c.isdigit()

def countdigit(st):
    """ This function count the number of digits 
        inside the input string
        
        >>> c = countdigit("abc1ab2c3")
        >>> print c
        3
        
        """
    return len([c for c in st if c.isdigit()]) 


def sumposnums(nums):
    return reduce(lambda x,y:x+y if y>=0 and x>=0 
                  else 0 if x<0 and y<0 else y if x<0 else x,nums)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    


