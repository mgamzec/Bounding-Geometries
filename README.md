# Bounding-Geometries

This repository contains a collection of Python scripts, each designed to perform a specific type of processing on polygon shapefiles. Whether you're looking to extract geometrical shapes, analyze spatial boundaries, or transform data, these scripts provide a range of functionalities to suit your needs.

Scripts Overview
Delaunay Triangulation (TRIANGULATION.py): Generates a Delaunay Triangulation from a given polygon shapefile, useful for spatial analysis and triangulating points in a plane.

Rotational Bounding Box (RO_BBOX.py): Calculates the rotational bounding box for a given polygon shapefile, which can be used in spatial data visualization and analysis.

Convex Hull Extraction (CONVEX_HULL.py): Creates the Convex Hull of a polygon shapefile. This is helpful in understanding the outer boundary of a shape or dataset.

Concave Hull Extraction (CONCAVE_HULL.py): Extracts the Concave Hull from a polygon shapefile, offering a tighter fitting boundary than the convex hull for irregular shapes.

Circle Extraction (CIRCLE.py): Determines the smallest enclosing circle for a given polygon shapefile, useful in various geometrical computations.

Bezier Envelope (BEZIER_ENVELOPE.py): Generates a Bezier Envelope from a polygon shapefile, which can be used for advanced geometrical representations and analyses.

Bounding Box (BBOX.py): Extracts the standard bounding box of a polygon shapefile, essential for many spatial analysis tasks.

Getting Started
To use these scripts, you'll need Python installed on your system along with libraries such as geopandas, shapely, scipy, numpy, and others specific to each script.

Prerequisites
Python 3.x
Libraries: geopandas, shapely, scipy.spatial, numpy, alphashape, smallestenclosingcircle, etc.
