#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 17:26:20 2018

@author: arabinov
"""

A = [1, 0, 1]
total = 0
ceros = 0
for i in A:
    if i == 0:
        ceros += 1
    else:
        total += ceros
print(total)