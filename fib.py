# -*- coding: utf-8 -*-
"""
Created on 12/05/16 11:44:14

fibonacci series

@author: Satoshi Murashige
"""

def fig(n):
    a,  b = 0.0,  1.0
    for i in range(n):
        a, b = a + b, a
    return a

