#!/usr/bin/python

import time
import sys

fo = open(sys.argv[1], 'r')
while True:
    line = fo.readline()
    
    if not line:
        time.sleep(1)
        fo.seek(fo.tell())
    else:
        print line,
