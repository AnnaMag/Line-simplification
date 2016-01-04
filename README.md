# Polyline simplification: process of reducing the resolution of a polyline

This is a by-product of my recent interest in digital maps.
In order to fully grasp the concepts, data types and experiment with methods and packages, I implemented this 'toy' example.

Line generalization refers to simplifying geometric lines (of any dimension)
by removing points. The points kept are those that retain good approximation
to the initial shapes, whilst reducing complexity and removing the least perceptible part. The areas of application include computer graphics and cartography.


This is an implementation of the Douglas-Peucker algorithm, which uses a point-to-edge distance as a measure of 'value' in preserving the shape:
>David H. Douglas and Thomas K. Peucker,
>“Algorithms for the Reduction of the Number of Points Required to Represent a >Digitized Line or its Caricature,” Cartographica: The International Journal for >Geographic Information and Geovisualization, vol. 10, Dec. 1973, pp. 112-122.

There is an additional option of running Radial Distance prior to the DP algorithm, which might prove useful in the presence of closely clustered points.

For demonstration, I used the data on GIS position of local buses
in Chicago extracted using its open API. The calculations assume a planar surface (relatively small spatial coverage of points).


###Future:
##### handle intersections

#####speed-up:
>J. Hershberger and J. Snoeyink. Speeding up the Douglas-Peucker line simplification >algorithm. In Proc. 5th Intl. Symp. Spatial Data Handling. IGU Commission on GIS, >pages 134--143, 1992. (home page).
##### Visvalingam’s algorithm,

Uses 'effective area' for Line simplification
>Line generalisation by repeated elimination of the smallest area Visvalingam, >Maheswari; Whyatt, J. D. (James Duncan) Cartography -- Data processing; Computer >science, July 1992

(visual intuition: http://bost.ocks.org/mike/simplify/)
