#!/usr/bin/python
import sys

print(sys.argv)
print >> sys.stdout , "simple out"
print >> sys.stderr , "simple error"
