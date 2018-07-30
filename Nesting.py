#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 18:36:48 2018

@author: andres
"""

S = '(()(())())'
S = '()(()()(((()())(()()))'

N = len(S)
size = 0
for s in range(N):
    if S[s] == '(':
        size += 1
    else:
        size -= 1
    if size < 0:
        print(0)
if size == 0:
    print(1)
else:
    print(0)
    
