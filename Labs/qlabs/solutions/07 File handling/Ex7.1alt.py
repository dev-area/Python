#!/usr/bin/python
# Chapter 7 Exercise 1 Alternative solution using a dictionary
import sys

if sys.platform == 'win32':
    file = r'C:\WINDOWS\system32\drivers\etc\services'
else:
    file = '/etc/services'

ports = dict()

for line in open(file, 'r'):
   
   if line[0:1] != '#' and not line.isspace():
       pp = line.split(None, 1)[1]
       port = pp.split ('/', 1)[0]
   
       port = int(port)
       ports[port] = None
       
       if port > 200: break 

for num in xrange(1,201):
    if not num in ports:
        print "Unused port", num