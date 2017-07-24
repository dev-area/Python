#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 17:40:55 2017

@author: parallels
"""

def addtax(val):
    return val*1.17

nums = [10,200,30]
inters = [1.17,1.18,1.16]

numstax = map(addtax,nums)

print numstax

numstax = map(lambda val:val*1.17,nums)

print numstax

numstax = map(lambda val,inter:val*inter,nums,inters)

print numstax

maxval = reduce(lambda a,b: a if (a > b) else b,nums)

print maxval

import re
codes = {}

names = ['zero','wun','two','tree','fower','fife','six','seven',
         'ait','niner','alpha','bravo','charlie','delta','echo',
         'foxtrot','golf','hotel','india','juliet','kilo','lima',
         'mike','november','oscar','papa','quebec','romeo',
         'sierra','tango','uniform','victor','whisky','xray',
         'yankee','zulu']

for key in (xrange(0,10)):
    codes[str(key)] = names[key]
for key in (xrange(ord('A'),ord('Z')+1)):
    codes[chr(key)] = names[key - ord('A')+10] 

reg = 'WG07 OKD'

result = re.sub(r'(\w)', 
                lambda m: codes[m.groups()[0]]+' ', reg)

testy = 'The quick brown fox the jumps over the lazy dog'

m = re.search(r"(quick|slow).*(the|camel)", testy)

