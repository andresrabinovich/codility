#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 21:33:12 2018

@author: andres
"""

A = [2, 2, 1, 2, 3, 1]
A.sort()
print(A)
resultado = 1
n = len(A)
if n == 0:
    resultado = 0
for i in range(n-1):
    print(i)
    if A[i] != A[i+1]:
        resultado += 1
print(resultado)