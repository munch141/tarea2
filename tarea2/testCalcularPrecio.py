'''
Created on Apr 26, 2016

@author: ricardo
'''
import unittest
import datetime
from decimal import Decimal
from calcularPrecio import Tarifa


class TestCalcularPrecio(unittest.TestCase):


    def setUp(self):
        self.t = Tarifa()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()