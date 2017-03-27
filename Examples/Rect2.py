# -*- coding: utf-8 -*-



class Rectangle:
    def __init__(self,width,height):
        self.__width = width
        self.__height = height
    def __PrintHeader(self):
        print("******************************************")
    def Print(self):
        self.__PrintHeader()
        print("Recangle Width:" + str(self.__width) + 
                    " Height:" + str(self.__height))
        
        
a = Rectangle(10,20)
a.Print()


a.__PrintHeader() # error
a.__height = -80  # new attribute
a.Print()




