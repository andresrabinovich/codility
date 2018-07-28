#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:11:23 2018

@author: arabinov
"""

A = [4, 3, 2, 7]
A.sort()
for i in range(len(A)):
    if i+1 != A[i]:
        print(0)
print(1)