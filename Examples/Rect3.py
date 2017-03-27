# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 16:43:51 2014

@author: liran
"""

class Rectangle:
    def __init__(self,width,height):
        self.__width = width
        self.__height = height
    def SetSize(self,new_width,new_height):
        if new_width > 0:
            self.__width = new_width
        if new_height > 0:
            self.__height = new_height
            
    def Print(self):
        print("Recangle Width:" + str(self.__width) + 
                    " Height:" + str(self.__height))
        
class RoundedRectangle(Rectangle):
    def __init__(self,width,height,angle):
        Rectangle.__init__(self,width,height)
        self.__angle = angle
    def SetAngle(self,angle):
        self.__angle = angle
    def Print(self):
        Rectangle.Print(self)
        print("RecangleX angle:" + str(self.__angle))
    
a = Rectangle(10,20)
b = RoundedRectangle(8,9,7)
a.Print()
b.Print()
b.SetSize(1000,2000)
b.Print()