#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 15:18:23 2017

@author: parallels
"""

import demopack.chelpers
import cProfile
cProfile.run("demopack.chelpers.countuppers('kPPk')")#, 'start.prof')
#cProfile.run("demopack.chelpers.countuppers('kPPk')", 'start.prof')
#python -m pstats start.prof