#! /usr/bin/env python
"""
Created on Mon Jan 4 2016
Anna M. Kedzierska
"""
import geojson

def create_map(points, type_obj, out_file_name):
    """
    Input: list of points as tuples, type_obj= 0: points, else: line
    Returns a GeoJSON file.
    Note: GitHub can automatically render the GeoJSON
    file as a map.
    """

    # Define type of GeoJSON we're creating
    geo_map = {"type": "FeatureCollection"}

    # Define empty list to collect each point
    item_list = []
    index = 0
    # Iterate over our data to create GeoJSOn document.

    for point in points:
        index = index + 1
        # beware of 0's
        if point[0] == "0" or point[1] == "0":
            continue

        data = {}
        data['type'] = 'Feature'
        data['id'] = 'Stop: '+ str(index)
        data['geometry'] = {'type': 'Point',
                            'coordinates': (point[0], point[1])}

        item_list.append(data)

    for point in item_list:
        geo_map.setdefault('features', []).append(point)

    with open(out_file_name + '.geojson', 'w') as f:
        f.write(geojson.dumps(geo_map))
