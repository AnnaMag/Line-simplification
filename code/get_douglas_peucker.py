#! /usr/bin/env python
"""
Created on Mon Jan 4 2016
Anna M. Kedzierska

Two implementations of the algorithm
"""
import numpy as np
from definitions import Line
from calculate_distance import CalculateDistance

def get_douglas_peucker_recursive(points, threshold):
    """
    Recursive version of the DP algorithm
    """
    xmax = 0.0 # floats
    xindex = 0

    L =len(points)

    TabLines = np.empty(L,dtype=Line)
    TabLines.fill(Line(points[0], points[-1]))
    # alternative for python3: list comprehensions?
    x = list(map(CalculateDistance.get_dist, TabLines, points))
    xmax = max(x)

    xindex = np.argmax(x)

    if xmax >= threshold:
        # [:-1] index is set no to add the same element, which appears in the set from the same split
        results = get_douglas_peucker_recursive(points[:xindex+1], threshold)[:-1] + get_douglas_peucker_recursive(points[xindex:], threshold) # adding sets (left and right split)
    else:
        results = [points[0], points[-1]] # collect the segments with no points above the threshold (no more splits)

    return results

    def get_douglas_peucker(points, tolerance):
        """calculate DP simplification: long initial version"""

        length = len(points)
        simplified = np.empty(length, dtype=int)

        first = 0
        last = length - 1

        #lists of the beg and ends of segments
        first_list = []
        last_list = []

        new_points = []

        # add beg and end to the keys
        simplified[first] = 1
        simplified[last] = 1

        while last:
            max_dist = 0

            for i in range(first, last):

                dist = CalculateDistance.get_dist(Line(points[first],points[last]), points[i])

                # find point that's futherest from the line and save its index
                if dist > max_dist:
                    index = i
                    max_dist = dist

            if max_dist > tolerance:
                # mark the point
                simplified[index] = 1

                first_list.append(first)
                last_list.append(index)

                first_list.append(index)
                last_list.append(last)

            if len(first_list) == 0:
                first = None
            else:
                first = first_list.pop()


            if len(last_list) == 0:
                last = None
            else:
                last = last_list.pop()

        # copy the marked points as keys (marked by 1, else is 0)
        for i in range(length):
            if simplified[i]:
                new_points.append(points[i])

        return new_points
