#! /usr/bin/env python
"""
Created on Mon Jan 4 2016
Anna M. Kedzierska

usage of the main function CalculateDistance.get_dist(Line([0,2],[3,2]), (2,4))
"""
from definitions import Line, PointLoc
import math_definitions
import math
from functools import singledispatch
from math_definitions import dot_product

class CalculateDistance(object):

    @singledispatch
    def get_dist(shape, point):
        pass

    @get_dist.register(PointLoc)
    def _(arg, point):
        """distance between two points"""
        dx = arg.x - point.x
        dy = arg.y - point.y

        return math.hypot(dx, dy)

    @get_dist.register(Line)
    def _(arg, point):
        """distance between a point and a segment"""
        point = PointLoc(point)
        dvx = arg.end[0] - arg.start[0]
        dvy = arg.end[1] - arg.start[1]
        #distance to the first point
        dwx = point.x - arg.start[0]
        dwy = point.y - arg.start[1]

        v = [dvx, dvy]
        w = [dwx, dwy]
        # c1/2 is an area of the triangle
        c1 = dot_product(w,v)

        # check if the 1st end of the segment is the closest of all (the sign of the dot products checks the side of the points)
        if c1 <= 0:
          return math.hypot(dwx,dwy)

        c2 = dot_product(v,v)
        #distance of the point to the second end of the segment, which is closer then the 1st
        if c2 <= c1:
          dzx = point.x - arg.end[0]
          dzy = point.y - arg.end[1]
          return math.hypot(dzx, dzy)

        # none of the endpoints is closest to he point, so calculate the projection onto the segment
        b = c1 / c2
        proj1 = arg.start[0] + b * v[0]
        proj2 = arg.start[1] + b * v[1]
        out = math.hypot(point.x - proj1, point.y - proj2)

        return out
