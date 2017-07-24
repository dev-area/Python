#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 17:20:38 2017

@author: parallels
"""

# Using the generator pattern (an iterable)
class firstn(object):
    def __init__(self, n):
        self.n = n
        self.num, self.nums = 0, []

    def __iter__(self):
        #self.num, self.nums = 0, []
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        else:
            raise StopIteration()

sum_of_first_n1 = sum(firstn(1000000))


# a generator that yields items instead of returning a list
def firstnfun(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n2 = sum(firstnfun(1000000))

# Note: Python 2.x only
# using a non-generator
sum_of_first_n3 = sum(range(1000000))

# using a generator
sum_of_first_n4 = sum(xrange(1000000))

doubles = [2 * n for n in range(50)] # list

doubles = (2 * n for n in range(50)) # gen

doubles = list(2 * n for n in range(50)) #list
# Note: Python 2.x only
#s = sum(xrange(1000000))
#p = product(xrange(1000000))