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
    ini = tiempoDeTrabajo[0]
    fin = tiempoDeTrabajo[1]
    
    t = fin - ini
    t = t.total_seconds()
    
    if t < 900:
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
        precio += (ini.weekday() < 5)*tarifa.sem + (4 < ini.weekday())*tarifa.fin
        ini += t
        
    return precio