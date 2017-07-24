#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 11:06:07 2017

@author: parallels
"""

with open("/etc/services","r") as f:
    for line in f:
        if line.startswith('#') or line.isspace():
            continue
        servcie , pp = line.split(None,1)
        ports,protocol = pp.split('/',1)
        port = int(ports)
        if port>200:
            break
        print port,protocol
        
        
        