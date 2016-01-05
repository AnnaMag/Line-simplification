# Polyline simplification: reducing the resolution

This is a by-product of my recent interest in digital maps.

Line generalization refers to simplifying geometric lines (of any dimension)
by removing points. The points kept are those that retain good approximation
to the initial shapes, whilst reducing complexity and removing the parts least perceptible to the human eye. When it comes to designing methods and algorithms to deal with such questions, applications in cartography are a true exploration playground.

This is an implementation of the Douglas-Peucker algorithm, which uses a point-to-edge distance as a measure of 'value' in preserving the shape:
>David H. Douglas and Thomas K. Peucker, “Algorithms for the Reduction of the Number of Points Required to Represent a Digitized Line or its Caricature,” Cartographica: The International Journal for Geographic Information and Geovisualization, vol. 10, Dec. 1973, pp. 112-122.

In addition, there is an option of running Radial Distance prior to the DP algorithm, which might prove useful in the presence of closely clustered points.

For demonstration, I used the data on Metro GIS positions in LA extracted using its open API (http://developer.metro.net/). The calculations assume a planar surface (relatively small spatial coverage of points) and no transformation of coordinates for the geo data was done (yet).

## Usage and notes
Coded in Python3 (otherwise bit to be modified: shapely and functools)
Run as
```
python run_line_simplification.py
```
The output includes a plot of the metro bus route for visual inspection and geojson files with the initial and pruned coordinates, which can be directly rendered in Gist

###Future:
#####Self-interections
e.g.
>The Douglas-Peucker Algorithm: Sufficiency Conditions for Non-Self-Intersections
Shin Ting Wu, Adler C. G. da Silva, Mercedes R. G. Márquez

#####Efficiency:
>J. Hershberger and J. Snoeyink. Speeding up the Douglas-Peucker line simplification algorithm. In Proc. 5th Intl. Symp. Spatial Data Handling. IGU Commission on GIS, pages 134--143, 1992. (home page).

#####Visvalingam’s algorithm
Uses the 'effective area' for line simplification. 'area_calculations' are already implemented
>Line generalisation by repeated elimination of the smallest area Visvalingam, Maheswari; Whyatt, J. D. (James Duncan) Cartography -- Data processing; Computer science, July 1992

(visual intuition: http://bost.ocks.org/mike/simplify/)
