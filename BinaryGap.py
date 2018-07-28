#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:07:35 2018

@author: arabinov
"""
N  = 9
bN = '{0:b}'.format(N)
print(bN)
contador = 0
maximo   = 0
for i in range(len(bN)):
    if bN[i] == '1': #Llegué a un límite
        if contador != 0: #Es el límite de la izquierda o de la derecha?
            if contador > maximo:
                maximo = contador
            contador = 0
    else:
        contador += 1
print(maximo)        
    