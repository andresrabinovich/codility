#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:46:05 2018

@author: arabinov
"""

A  = [3, 4, 4, 6, 1, 4, 4]
N  = 5
C  = [0]*N
maximo =  0
offset =  0

for comando in A:
    if(comando <= N):
        if offset > C[comando-1]:
                C[comando-1] = offset        
        C[comando-1] += 1
        if maximo < C[comando-1]:
            maximo = C[comando-1]
    else:
        offset = maximo
    
for i in range(len(C)):
    if C[i] < offset:
        C[i] = offset
print(C)

