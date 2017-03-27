# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 15:32:52 2014

@author: liran
"""


class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def Print(self):
        print("Recangle Width:" + str(self.width) + 
                    " Height:" + str(self.height))
        
a = Rectangle(10,20)

a.Print()




