# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:21:11 2015

@author: liran
"""

x=open('emp.txt','r')
d=dict()
emps=[]
s= x.readlines()

for i in range(len(s)):
    j=s[i].split(",")
    d['id']=j[0]
    d['name']=j[1]
    d['sal']=j[2]
    emps+=[d.copy()]
    
print emps


