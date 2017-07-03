#!/usr/bin/python
# Python 2 version

y = int(raw_input ('Please enter a year :'))
            
if y % 4 == 0 and (y % 400 == 0 or y % 100 != 0):
    print "Leap Year" 
else:
    print "NOT a leap year" 
 