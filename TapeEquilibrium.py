#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 12:27:41 2018

@author: arabinov
"""

A = [3, 1]

izquierda = A[0]
derecha   = sum(A[1:len(A)])
diferencia_menor = abs(izquierda-derecha)
for p in range(1, len(A)-1):
    izquierda += A[p]
    derecha   -= A[p]
    diferencia = abs(izquierda-derecha)
    print(diferencia)
    if diferencia < diferencia_menor:
        diferencia_menor = diferencia
print(diferencia_menor)

