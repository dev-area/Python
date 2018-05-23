#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class A(object):
    def __init__(self):
        print('Running A.__init__')
        super(A,self).__init__()

class B(A):
    def __init__(self):
        print('Running B.__init__')   
        super(B,self).__init__()

class C(A):
    def __init__(self):
        print('Running C.__init__')
        super(C,self).__init__()

class D(B,C):
    def __init__(self):
        print('Running D.__init__')
        super(D,self).__init__()

foo=D()

