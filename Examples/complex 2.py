# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 13:17:27 2014

@author: liran
"""

import numpy as np


class Complex:
    nums=0
    @staticmethod
    def mystatic():
        print 'static'
    def __init__(self,real = 0,img = 0):
        self.ginit(real,img)
    def ginit(self,r,i):
        self.__real = r
        self.__img = i
        Complex.nums+=1
    def f1(self):
        print "f1 A"
        self.f2()
    def f2(self):
        print "f2 A"
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
                    str1 + str(num) + "i " + str(Complex.nums))

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
    def f2(self):
        print "f2 B"
    def SetReal(self,new_real):
        if(new_real > 0):
            Complex.SetReal(self,new_real)
            
    def SetImg(self,new_img):
        if (new_img > 0):
            Complex.SetImg(self,new_img)
            
    
a = Complex(10,-20)
b = PComplex(9,7)
b.f1()

Complex.mystatic()

x=[a,b,b,a]
for s in x:
    s.Print()
    
'''
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

'''


