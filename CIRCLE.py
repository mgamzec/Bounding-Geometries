'''
THE GOAL OF THIS PYTHON SCRIPT IS TO EXTRACT A CIRCLE OUT OF AN INPUT POLYGON SHAPEFILE
'''

import geopandas as gpd
from shapely.geometry import Point, Polygon
from smallestenclosingcircle import make_circle

# Load the shapefile
gdf = gpd.read_file("pincodebndry.shp")

# Combine all the polygons into a single MultiPolygon
multipolygon = gdf.unary_union

# Get the coordinates of the multipolygon
coords = list(multipolygon.exterior.coords)

# Calculate the smallest enclosing circle
center_x, center_y, radius = make_circle(coords)

# Create a circle around the center with the calculated radius
circle = Point(center_x, center_y).buffer(radius)

# Create a new GeoDataFrame to save the circle
circle_gdf = gpd.GeoDataFrame(geometry = [circle])

# Save the circle to a new shapefile
circle_gdf.to_file("BOUNDING/CIRCLE_2.shp")

# End of Python Script
print("TASK COMPLETED SUCCESSFULLY")
