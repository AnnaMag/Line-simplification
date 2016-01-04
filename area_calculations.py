#! /usr/bin/env python
"""
Created on Mon Jan 4 2016
Anna M. Kedzierska
"""

def GetArea(p0, p1, p2):
    # Note to self: the area of a planar parallelogram or triangle can be expressed
    #by the magnitude of the cross-product of two edge vectors: 0.5|v x w|, v = w,
    vx = p1.x - p0.x
    vy = p1.y - p0.y

    wx = p2.x - p0.x
    wy = p2.y - p0.y


    v = [vx, vy]
    w = [wx, wy]
    area = 0.5 * np.cross(w,v)
    #explicit formulae: vx*wy-wx*vy
    # we leave the sign becase it adds info on the 'direction' of the point
    return area
