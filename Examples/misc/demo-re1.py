#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 21:13:15 2017

@author: parallels
"""
import re
testy = 'The quick brown fox jumps over the lazy dog'

m = re.search(r"(quick|slow).*(fox|camel)", testy)
if m:
    print 'Matched',m.groups()
    print 'Starting at', m.start()
    print 'Ending at', m.end()
