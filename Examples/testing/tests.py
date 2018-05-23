#from nose2.tools import params
from parameterized import parameterized

from p1 import *
import unittest


def test_f2():
    res = f2(2, 5)
    assert res == 7



@parameterized([(1, 2, 13), (3, 4, 7)])
def test_f2_params(a, b, c):
    res = f2(a, b)
    assert res == c

    #  pycharm runner will not work because it uses nosetests instead of nose2 : working from terminal: nose2 -v
    # class Test(unittest.TestCase):
    #
    #     @params((1, 2), (2, 3), (4, 5))
    #     def test_less_than(self, a, b):
    #         assert a < b

class Test1(unittest.TestCase):
    @parameterized.expand([(2, 3), (3, 4)])
    def test_less_than(self, a, b):
          assert a < b
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

class Test2(unittest.TestCase):
    @parameterized.expand([("with:2,3",2, 3), ("with:3,4",3, 4)])
    def test_less_than(self,_,a, b):
          assert a < b
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
