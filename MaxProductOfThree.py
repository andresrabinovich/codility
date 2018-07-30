#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 21:49:01 2018

@author: andres
"""

A = [-3, 1, 2, -2, 5, 6]
A = [-5, 5, -5, 4]
A = [-4, -6, 3, 4, 5]
A = [-5, -6, -4, -7, -10]
A = [4, 7, 3, 2, 1, -3, -5]
A.sort()
resultado = A[-3]*A[-2]*A[-1]
if A[-1]*A[0]*A[1] > resultado:
    resultado = A[-1]*A[0]*A[1]
print(resultado)