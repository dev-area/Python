#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 08:39:59 2017

@author: parallels
"""

filename = "foo"
errmsg=""
try: 
   # raise SystemExit,"aaa"
    exit("get out")
    f = open(filename) 
#except (IOError,SystemExit),var:
#    print var
except Exception:
    errmsg = "Could not open foo"
except (TypeError,ValueError):
    errmsg = "Invalid filename"   
except SystemExit:
    errmsg =  'Exist called'
if errmsg != "":
    print errmsg
print "end"

