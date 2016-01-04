#! /usr/bin/env python
"""
Created on Mon Jan 4 2016
Anna M. Kedzierska
"""
import numpy as np
from numpy import dot

def check(v1,v2):
    if len(v1)!=len(v2):
        raise ValueError("the length of both vectors/arrays must be the same")
    pass

def cross_product(v1, v2):
    check(v1, v2)
    return np.cross(v1, v2)

def dot_product(v1, v2):
    check(v1, v2)
    return np.dot(v1, v2)
