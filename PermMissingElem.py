#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 12:10:20 2018

@author: arabinov
"""

A = [1, 2]
if len(A) > 0:
    A.sort()
    for i in range(len(A)):
        if i+1 != A[i]:
            print(i+1)
    print(len(A) + 1)
else:
    print(1)