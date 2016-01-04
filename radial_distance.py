#! /usr/bin/env python
"""
Created on Mon Jan 4 2016
Anna M. Kedzierska
"""
from definitions import Point_loc

def EstimateRadialDistance(inLine, tolerance):

  def RadialDist_myReduce(resultsList, elem):
     if len(resultsList)==0:
           resultsList = [elem]

     lastElem = resultsList[-1]

     if CalculateDistance.get_dist(Point_loc(lastElem), Point_loc(elem)) > tolerance:

        return resultsList + [elem]

     else:

        return resultsList

  return reduce(RadialDist_myReduce, inLine, [])
