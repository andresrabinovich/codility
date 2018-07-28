#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:14:14 2018

@author: arabinov
"""

A = [1, 3, 1, 2, 4, 5, 3, 4, 7, 8, 1, 9, 11, 4, 12, 1, 13, 10, 1, 2, 6, 3, 4]
X = 7
if(len(A) < X):
    print(-1)
else:
    A_aux = [0] * len(A)
    total = 0
    for i in range(len(A)):
        if A[i] <= X and A_aux[A[i]-1] == 0 :
           A_aux[A[i]-1] = 1
           total += 1
        if total == X:
            print(i)
    print(-1)
    
