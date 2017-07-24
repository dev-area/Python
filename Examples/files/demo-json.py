#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 19:29:17 2017

@author: parallels
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 18:21:10 2017

@author: parallels
"""

import json

class Account: 
    numCreated = 0
    def __init__(self, initial):
        self.__balance = initial 
        self.list = [1,2,3]
        Account.numCreated += 1
    def deposit(self, amt):
        self.__balance = self.__balance + amt 
        self.list+=[self.__balance]
    def withdraw(self,amt):
        self.__balance = self.__balance - amt 
    def getbalance(s):
        return s.__balance
    def getlist(self):
        return self.list

class AccountEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Account):
            return '{Balance:%d}'% obj.getbalance() 
        return json.JSONEncoder.default(self, obj)

a = Account(10)

a.deposit(10)

d = open("nums.json",'w')
#list = ['foo', {'bar': ('baz', None, 1.0, 2)}]

json.dump(a,d,cls=AccountEncoder)

#json.dump(a.__dict__,d)

d.close()

print list