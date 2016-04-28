'''
Created on Apr 26, 2016

@author: ricardo
'''
import unittest
import datetime
from calcularPrecio import *


class TestCalcularPrecio(unittest.TestCase):
    
    def testTimedelta15min(self):
        tarifa = Tarifa(1,1)
        ini = datetime.datetime(2016, 4, 1, 7, 0)
        fin = datetime.datetime(2016, 4, 1, 7, 15)
        self.assertEqual(1, calcularPrecio(tarifa, [ini, fin]))
        
    def testTimedelta7dias(self):
        tarifa = Tarifa(1,1)
        ini = datetime.datetime(2016, 4, 1, 7, 0)
        fin = datetime.datetime(2016, 4, 8, 7, 0)
        self.assertEqual(168, calcularPrecio(tarifa, [ini, fin]))
        
    def testTarifaSem0(self):
        tarifa = Tarifa(0,1)
        ini = datetime.datetime(2016, 4, 1, 7, 0)
        fin = datetime.datetime(2016, 4, 8, 7, 0)
        self.assertEqual(24*2, calcularPrecio(tarifa, [ini, fin]))
        
    def testTarifaFinSem0(self):
        tarifa = Tarifa(1,0)
        ini = datetime.datetime(2016, 4, 1, 7, 0)
        fin = datetime.datetime(2016, 4, 8, 7, 0)
        self.assertEqual(24*5, calcularPrecio(tarifa, [ini, fin]))
        
    def testTimedeltaEntre15y0(self):
        tarifa = Tarifa(1,1)
        ini = datetime.datetime(2016, 4, 1, 7, 0)
        fin = datetime.datetime(2016, 4, 1, 7, 5)
        self.assertEqual(0, calcularPrecio(tarifa, [ini, fin]))
        
    def testTimedeltaMayorA7Dias(self):
        tarifa = Tarifa(1,1)
        ini = datetime.datetime(2016, 4, 1, 7, 0)
        fin = datetime.datetime(2016, 4, 15, 7, 0)
        self.assertEqual(168, calcularPrecio(tarifa, [ini, fin]))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()