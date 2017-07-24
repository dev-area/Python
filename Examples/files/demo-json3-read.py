import json

class Account: 
    def __init__(self, initial):
        self.__balance = initial 
    def deposit(self, amt):
        self.__balance = self.__balance + amt 
    def withdraw(self,amt):
        self.__balance = self.__balance - amt 
    def getbalance(s):
        return s.__balance
   

def as_account(dct):
    if 'Balance' in dct:
        return Account(dct['Balance'])
    return dct
    

with open('accounts.json','r') as d:
    accs=json.load(d,object_hook=as_account)


#
#c=json.loads('{"Balance": 100}',
#    object_hook=as_account)