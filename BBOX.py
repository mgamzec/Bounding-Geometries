'''
THE GOAL OF THIS PYTHON SCRIPT IS TO EXTRACT THE BOUNDING BOX OUT OF AN INPUT POLYGON SHAPEFILE
'''

import geopandas as gpd
from shapely.geometry import Polygon

# Load the input shapefile
input_gdf = gpd.read_file("pincodebndry.shp")

# Get the total bounding box of all features
total_bounds = input_gdf.total_bounds

# Create a polygon from the bounding box
bbox_poly = Polygon([
    (total_bounds[0], total_bounds[1]),
    (total_bounds[0], total_bounds[3]),
    (total_bounds[2], total_bounds[3]),
    (total_bounds[2], total_bounds[1]),
])

# Create a GeoDataFrame from the polygon
bbox_gdf = gpd.GeoDataFrame({'id': ['bbox']}, geometry = [bbox_poly], crs = input_gdf.crs)

# Save to a new shapefile
bbox_gdf.to_file("BOUNDING/bbox.shp")

# End of the Python Script
print("TASK COMPLETED SUCCESSFULLY")
