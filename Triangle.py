#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 14:21:45 2018

@author: andres
"""

def solution(A):
    A.sort()
    N = len(A)
    for P in range(N-2):
        if A[P] + A[P + 1] > A[P + 2] and A[P + 1] + A[P + 2] > A[P] and A[P + 2] + A[P] > A[P + 1]:
            return(1)
    return(0)
    

A = [10, 2, 5, 1, 8, 20]
A = [10, 50, 5, 1]
solution(A)