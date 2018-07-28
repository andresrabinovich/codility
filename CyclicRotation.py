#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 11:04:37 2018

@author: arabinov
"""

A = [3, 8, 9, 7, 6]
K = 3
if len(A) == 0:
    print(A)
for i in range(K):
    A.insert(0, A[-1])
    A.pop(-1)
print(A)