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
            return {'Balance' :obj.getbalance()}
        return json.JSONEncoder.default(self, obj)

a = Account(123)
with open("account.json",'w') as d:
    a = json.dump(a,d,cls=AccountEncoder)