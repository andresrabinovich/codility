#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 14:55:40 2018

@author: andres
"""

A = [1, 5, 2, 1, 4, 0]
events = []
for i, a in enumerate(A):
    events += [(i-a, +1), (i+a, -1)]
events.sort(key=lambda x: (x[0], -x[1]))    
intersections, active_circles = 0, 0

for _, circle_count_delta in events:
    intersections += active_circles * (circle_count_delta > 0)
    active_circles += circle_count_delta
    if intersections > 10E6:
        print(-1)
print(intersections)