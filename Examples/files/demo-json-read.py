

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

def as_account(dct):
    return Account(dct['Balance'])


d = open("nums.json",'r')

a = json.load(d, object_hook=as_account)


#a = Account(10)
#a.__dict__ = json.load(d)

d.close()

print a