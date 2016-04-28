'''
Created on Apr 26, 2016

@author: ricardo
'''
import unittest
import datetime
from calcularPrecio import *


class TestCalcularPrecio(unittest.TestCase):
    
    def testTarifaSemNeg(self):
        tarifa = Tarifa(-1,1)
        ini = datetime.datetime(2016, 4, 1, 7, 0)
        fin = datetime.datetime(2016, 4, 3, 9, 0)
        self.assertEqual(-1, calcularPrecio(tarifa, [ini, fin]))
        
    def testTarifaFinSemNeg(self):
        tarifa = Tarifa(1,-1)
        ini = datetime.datetime(2016, 4, 1, 7, 0)
        fin = datetime.datetime(2016, 4, 3, 9, 0)
        self.assertEqual(-1, calcularPrecio(tarifa, [ini, fin]))
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    