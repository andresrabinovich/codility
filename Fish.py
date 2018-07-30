#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 19:27:35 2018

@author: andres
"""

def solution(A, B):
    go_up_count = 0
    s1 = []
    for i in range(0, len(A)):
        a = A[i]
        b = B[i]
        if b == 0:
            if not s1:
                go_up_count += 1
            else:
                while s1 and a > s1[-1]:
                    s1.pop()
                if not s1:
                    go_up_count += 1
        else:
            s1.append(a)

    return go_up_count + len(s1)    

    
A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 1, 0]

solution(A, B)
