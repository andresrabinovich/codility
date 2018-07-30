#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 15:31:54 2018

@author: andres
"""

A  = [4, 2, 2, 5, 1, 5, 8]
A = [10000, -10000]


resultado       = 0
minimo_promedio = max(A)

for i in range(len(A)-2):
    tajada_dos  = A[i]+A[i+1]
    tajada_tres = tajada_dos + A[i+2]
    tajada_dos  = tajada_dos/2
    tajada_tres = tajada_tres/3
    if tajada_dos < minimo_promedio:
        minimo_promedio = tajada_dos
        resultado = i
    if tajada_tres < minimo_promedio:
        minimo_promedio = tajada_tres
        resultado = i

tajada_dos      = (A[len(A)-2]+A[len(A)-1])/2       
if tajada_dos < minimo_promedio:
    minimo_promedio = tajada_dos
    resultado = len(A)-2 

print(resultado)
