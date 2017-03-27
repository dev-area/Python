# -*- coding: utf-8 -*-



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
c = Rectangle(40,50)

mylist = [a,b,c]

for x in enumerate(mylist):
    x[1].Print()
    


