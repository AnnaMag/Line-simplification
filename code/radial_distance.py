#! /usr/bin/env python
"""
Created on Mon Jan 4 2016
Anna M. Kedzierska
"""
from definitions import PointLoc

def estimate_radial_distance(inLine, tolerance):

  def radial_dist_myReduce(resultsList, elem):
     if len(resultsList)==0:
           resultsList = [elem]

     lastElem = resultsList[-1]

     if CalculateDistance.get_dist(PointLoc(lastElem), PointLoc(elem)) > tolerance:

        return resultsList + [elem]

     else:

        return resultsList

  return reduce(radial_dist_myReduce, inLine, [])
