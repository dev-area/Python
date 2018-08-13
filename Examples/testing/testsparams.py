#   pycharm runner using nosetests instead of nose 2,: working from terminal: nose2 -v

from nose2.tools import params
import unittest

@params(1, 2, 3)
def test_nums(num):
    assert num < 4


class Test(unittest.TestCase):
     @params((1, 2), (2, 3), (4, 5))
     def test_less_than(self, a, b):
         assert a < b
