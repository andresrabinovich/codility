#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 11:12:09 2018

@author: arabinov
"""
from collections import Counter
A = [9, 3, 9, 3, 9, 7, 9]
D = Counter(A)
for indice, cantidad in D.items():
    if cantidad % 2 == 1:
        print (indice)
        