# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 11:38:43 2022

@author: ASUS
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importar datos
dataset = pd.read_excel('Copia de Datos Corte # 2.xlsx')

#variable independiente en matriz
D=dataset.iloc[:,[1,2]]
#variables dependiente en matriz 
U=dataset.iloc[:,3]

prom = (U)/5
print (prom)

#cuando pongamos este simbolo, delimitamos la zona ejecutada
#definimos un vector con 50 nodos equiespaciados en [-1,1]:
D = np.linspace(-1, 1)

#ahora calculamos otro vector cuyas coordenadas son el coceno de las U

U = np.cos(D)

plt.plot(D,U)







