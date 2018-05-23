#!/usr/bin/env python3
# -*- coding: utf-8 -*-



class Singleton(type): 
    _instances = {}
    def __init__(self,a,b,c):
        print("new",a,b,c)
    def __call__(cls, *args, **kwargs):
        print(cls)
        print(args)
        print(kwargs)
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class A(object):
    def __init__(self,val):
        self.__v = val
        print("new A")
    def show(self):
        print(self.__v)

#Python3
class SingleA(A, metaclass=Singleton): 
    pass

a1=SingleA(10)

a2=SingleA(20)