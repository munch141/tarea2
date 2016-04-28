'''
Created on Apr 26, 2016

@author: ricardo
'''

import math
import datetime
from decimal import Decimal

class Tarifa:
    def __init__(self, t_sem, t_fin):
        self.sem = Decimal(t_sem)
        self.fin = Decimal(t_fin)

def calcularPrecio(tarifa, tiempoDeTrabajo):
    '''
    El dominio de datos de calcularPrecio es el conjunto de tuplas de numeros
    reales positivos unido al conjunto de tuplas de fechas validas donde la
    segunda fecha es posterior a la primera.
    '''
    if tarifa.sem < 0 or tarifa.fin < 0:
        print("Error: las tasas de la tarifa no pueden ser negativas.")
        return -1
    
    ini = tiempoDeTrabajo[0]
    fin = tiempoDeTrabajo[1]
    
    t = fin - ini
    t = t.total_seconds()
    
    if t < 900:
        if t < 0:
            horas = -1
        else:
            horas = 0
    elif 604800 < t:
        horas = 168
    else:
        horas = int(math.ceil(t / 3600))
    
    if horas < 0:
        print("Error: fecha de inicio posterior a fecha de fin.")
        return -1
    
    t = datetime.timedelta(hours = 1)
    precio = 0

    for i in range(horas):
        if ((ini.weekday() == 4) and ((ini+t).weekday() == 5)) or \
           ((ini.weekday() == 6) and ((ini+t).weekday() == 0)):
            precio += tarifa.sem + tarifa.fin
        else:
            precio += (ini.weekday() < 5)*tarifa.sem + \
                      (4 < ini.weekday())*tarifa.fin
        ini += t
        
    return precio