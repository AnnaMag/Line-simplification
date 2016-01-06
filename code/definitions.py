#! /usr/bin/env python
"""
Created on Mon Jan 4 2016
Anna M. Kedzierska

"""
class PointLoc:
    def __init__(self, p):
        self.x, self.y  = p[0], p[1]
class Line:
    def __init__(self, start, end):
        self.start, self.end = start, end
