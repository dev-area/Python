#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 14:32:01 2017

@author: parallels
"""

import sys
sys.stdout.write("Please enter a value:")
sys.stdout.flush()
reply =  sys.stdin.readline().rstrip()
print "<",reply,"> was input"
