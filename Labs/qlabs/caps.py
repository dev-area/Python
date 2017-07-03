#!/usr/bin/python

fh = open ("..\..\country.txt", "r")

for line in fh.readlines():
    (country,capital) = line.split(',')[0:3:2]
    print country,capital

fh.close()