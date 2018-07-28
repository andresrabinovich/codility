#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 17:41:16 2018

@author: arabinov
"""
import math
A = 11
B = 345
K = 17
total = math.floor(B/K)-math.floor(A/K)
if A%K == 0:
    total += 1   
print(total)
