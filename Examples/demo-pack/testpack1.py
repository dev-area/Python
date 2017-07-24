#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 12:21:02 2017

@author: parallels
"""



import demopack.chelpers
import demopack.numhelpers


print demopack.chelpers.countuppers('kPPk')
print demopack.chelpers.countuppers('kPPk');

print demopack.numhelpers._isdigit('2')

print help(demopack.numhelpers)

#########################################################

#use __all__ for import only public interface

#from demopack import *
#
#print chelpers.countuppers('kPPk')

### error when using numhelpers
#print demopack.numhelpers.countdigit('fds43fd32');

#print demopack.numhelpers.__isdigit('2')  


####################################################

# manulay import


#from demopack.chelpers import *
#from demopack.numhelpers import *
#
#print countuppers('kPPk')
#print countdigit('fds43fd32');
#
#print _isdigit('2')  #ERROR