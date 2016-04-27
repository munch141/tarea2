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
        self.tarifa = Tarifa(1,1)
        self.ini = datetime.datetime(2016, 04, 01, 07, 00)
        self.fin = datetime.datetime(2016, 04, 01, 07, 15)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()