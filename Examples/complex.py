# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 13:17:27 2014

@author: liran
"""

import numpy as np


class Complex:
    def __init__(self,real = 0,img = 0):
        self.__real = real
        self.__img = img
    def SetReal(self,new_real):
        self.__real = new_real
    def SetImg(self,new_img):
        self.__img = new_img  
    def GetReal(self):
        return self.__real   
    def GetImg(self):
        return self.__img        
    def Print(self):
        if(self.__img >=0):
            str1 = " + "
            num = self.__img
        else:
            str1 = " - "
            num = self.__img * -1
        print("Complex " + str(self.__real) + 
                    str1 + str(num) + "i")

class PComplex(Complex):
    def __init__(self,real = 0,img = 0):
        if(real > 0 ):
            lreal = real
        else:
            lreal = 0
        if(img > 0):
            limg = img
        else:
            limg = 0
        Complex.__init__(self,lreal,limg)
    def SetReal(self,new_real):
        if(new_real > 0):
            Complex.SetReal(self,new_real)
            
    def SetImg(self,new_img):
        if (new_img > 0):
            Complex.SetImg(self,new_img)
    

    
a = Complex(10,-20)
b = Complex(9,7)

a.Print()
a.SetReal(100)
a.Print()
c = a + b

c.Print()

aa = np.array([a, b], object)
bb = np.array([a, b], object)
v=aa+bb

print(v[0].GetReal())
v[1].Print()




