#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:00:54 2018

@author: arabinov
"""
A = [-1, -3, 0, 458]
A_aux = [0] * max(A)
if len(A_aux) == 0:
    print(1)
total = 0
for i in range(len(A)):
    if A[i] > 0:
        A_aux[A[i]-1] = 1

for i in range(len(A_aux)):
    if A_aux[i] == 0:
        print(i+1)
print(i+2)