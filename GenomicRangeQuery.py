#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 13:09:36 2018

@author: andres
"""
def prefix_sums(A):
    n = len(A)
    P = [[0]*(n + 1), [0]*(n + 1), [0]*(n + 1), [0]*(n + 1)]
    for k in range(1, n + 1):
        P[0][k] = P[0][k - 1]
        P[1][k] = P[1][k - 1]
        P[2][k] = P[2][k - 1]
        P[3][k] = P[3][k - 1]
        if A[k - 1] == 'A':
            P[0][k] += 1
        if A[k - 1] == 'C':
            P[1][k] += 1
        if A[k - 1] == 'G':
            P[2][k] += 1
        if A[k - 1] == 'T':
            P[3][k] += 1
    return P

def count_total(P, x, y):
    return P[y + 1] - P[x]

Sa  = 'AC'
pS = prefix_sums(Sa)
P  = [0, 0, 1]
Q  = [0, 1, 1]
resultados = [0]*len(P)
for i in range(len(P)):
    if(count_total(pS[0], P[i], Q[i]) > 0):
        resultados[i] = 1
    elif(count_total(pS[1], P[i], Q[i]) > 0):
        resultados[i] = 2
    elif(count_total(pS[2], P[i], Q[i]) > 0):
        resultados[i] = 3
    elif(count_total(pS[3], P[i], Q[i]) > 0):
        resultados[i] = 4        
print(resultados)

S  = 'CAGCCTA'
impact_factors = {'A':1, 'C':2, 'G':3, 'T':4}
P  = [2, 5, 0]
Q  = [4, 5, 6]
resultados = [0]*len(P)
for i in range(len(P)):
    s = S[P[i]:Q[i]+1]
    minimum_impact_factor = 5
    for j in range(len(s)):
        if impact_factors[s[j]] < minimum_impact_factor:
            minimum_impact_factor = impact_factors[s[j]]
    resultados[i] = minimum_impact_factor
print(resultados)

