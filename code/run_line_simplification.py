#! /usr/bin/env python
"""
Created on Mon Jan 4 2016
Anna M. Kedzierska
"""

from make_plots import lines_multiplot
from calculate_distance import  CalculateDistance
from radial_distance import estimate_radial_distance
from get_douglas_peucker import get_douglas_peucker_recursive
from create_geojson import create_map

import requests
import json
import geojson

def process_bus_data():
    """
    Extract and parse the data
    """
    res_request = requests.get("http://api.metro.net/agencies/%20lametro/routes/704/sequence/")
    #http://developer.metro.net/introduction/realtime-api-overview/realtime-api-returning-json/
    res_request.raise_for_status() # check the response object for errors
    data_req = res_request.json()
    i = 0
    loc_data =[]
    while i<len(data_req['items']):
        stops_lon = data_req['items'][i]['longitude']
        stops_lat = data_req['items'][i]['latitude']
        loc_data.append((stops_lon, stops_lat))
        i+=1
    return loc_data

tolerance = 0.003


def simplify_lineDP(points, tolerance, RadialPass):
    # if Radial Distance == True, it is run before DP
    if RadialPass:
        points = estimate_radial_distance(points, tolerance)
    points = get_douglas_peucker_recursive(points, tolerance)
    return points

# process the input data
loc_data = process_bus_data()
# simplify the polyline using the DP algorithm. Call with True if Radial Distance
# should be a pre-step
loc_data_simplified = simplify_lineDP(loc_data, tolerance, False)
# plot the results and save it in the bus_route.png
lines_multiplot(loc_data, loc_data_simplified, 'bus_route')

# create geojson files from the input and output data (to be ploted in Gist or
# for use with Leaflet)
create_map(loc_data,0, 'data_input')
create_map(loc_data_simplified, 1, 'data_output')
