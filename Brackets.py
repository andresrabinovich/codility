#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 18:36:38 2018

@author: andres
"""

def result(S):
    N = len(S)
    pila = ['']*N
    size = 0
    cierres = {'(':')', '{':'}', '[':']'}
    for s in S:
        if s == '(' or s == '{' or s == '[':
            pila[size] = s
            size += 1
        else:
            if size == 0:
                return(0)
            if cierres[pila[size - 1]] != s:
                return(0)
            else:
                size -= 1
    if size == 0:                
        return(1)
    else:
        return(0)

result("{[()()]}")
result("([)()]")
result("([)])")
result(")(")
