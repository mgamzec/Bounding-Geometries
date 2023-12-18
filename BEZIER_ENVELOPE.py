'''
THE GOAL OF THIS PYTHON SCRIPT IS TO EXTRACT A BEZIER ENVELOPE OUT OF AN INPUT POLYGON SHAPEFILE
'''

import os
import geopandas as gpd
from shapely.geometry import Polygon

# Load shapefile
gdf = gpd.read_file('pincodebndry.shp')

# Initialize a list for the bounding envelopes
bounding_polygons = []

# Iterate over the geometries and calculate the convex hull
for index, row in gdf.iterrows():
    # Get the convex hull of the geometry
    convex_hull = row.geometry.convex_hull
    # Add the polygon to the list
    bounding_polygons.append(Polygon(convex_hull.exterior.coords))

# Create a new GeoDataFrame for the bounding envelopes
bounding_gdf = gpd.GeoDataFrame(geometry=bounding_polygons)

# Make sure the CRS is the same as the original GeoDataFrame
bounding_gdf.crs = gdf.crs

# Create the output directory if it doesn't exist
if not os.path.exists('BOUNDING'):
    os.makedirs('BOUNDING')

# Save the bounding envelopes as a new shapefile
bounding_gdf.to_file('BOUNDING/BEZIER_ENVELOPE.shp')

# End of Python Script
print("TASK COMPLETED SUCCESSFULLY")
