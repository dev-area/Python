#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 19:08:28 2017

@author: parallels
"""

import shelve
db = shelve.open('dbs')
print db['names']
db.close()
