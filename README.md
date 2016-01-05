# Polyline simplification: reducing the resolution

This is a by-product of my recent interest in digital maps.

Line generalization refers to simplifying geometric lines (of any dimension)
by removing points. The points kept are those that retain good approximation
to the initial shapes, whilst reducing complexity and removing the parts least perceptible to the human eye. When it comes to designing methods and algorithms to deal with such questions, applications in cartography are a true exploration playground.

This is an implementation of the Douglas-Peucker algorithm, which uses a point-to-edge distance as a measure of 'value' in preserving the shape:
>David H. Douglas and Thomas K. Peucker,
>“Algorithms for the Reduction of the Number of Points Required to Represent a >Digitized Line or its Caricature,” Cartographica: The International Journal for >Geographic Information and Geovisualization, vol. 10, Dec. 1973, pp. 112-122.

In addition, there is an option of running Radial Distance prior to the DP algorithm, which might prove useful in the presence of closely clustered points.

For demonstration, I used the data on Metro GIS positions in LA extracted using its open API (http://developer.metro.net/). The calculations assume a planar surface (relatively small spatial coverage of points) and no transformation of coordinates for geo data was done (yet).

## Usage and notes
Coded for Python3 (otherwise bit to be modified: shapely and functools)

The main script
'''
python run_line_simplification.py
'''

###Future:
##### handle intersections
There are two instances that may cause problems in complex cases:
1. In the DP implementation itself: when line drawn between two key points crosses other lines (checking additional condition)
2. When the input polyline has knots it should be split into non-intersecting
polygons

#####speed-up:
>J. Hershberger and J. Snoeyink. Speeding up the Douglas-Peucker line simplification >algorithm. In Proc. 5th Intl. Symp. Spatial Data Handling. IGU Commission on GIS, >pages 134--143, 1992. (home page).

##### Visvalingam’s algorithm
Uses the 'effective area' for line simplification. 'area_calculations' are already implemented
>Line generalisation by repeated elimination of the smallest area Visvalingam, >Maheswari; Whyatt, J. D. (James Duncan) Cartography -- Data processing; Computer >science, July 1992

(visual intuition: http://bost.ocks.org/mike/simplify/)
