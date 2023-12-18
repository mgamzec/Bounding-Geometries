'''
THE GOAL OF THIS PYTHON SCRIPT IS TO EXTRACT THE ROTATIONAL BOUNDING BOX OUT OF AN INPUT POLYGON SHAPEFILE
'''

import geopandas as gpd

# Load the input shapefile
input_gdf = gpd.read_file("pincodebndry.shp")

# Merge all geometries in the GeoDataFrame into one
union_geometry = input_gdf.unary_union

# Compute the minimum rotated rectangle of the union
min_rotated_rect = union_geometry.minimum_rotated_rectangle

# Create a new GeoDataFrame with the minimum rotated rectangle
# Use 'id' as column name instead of 1
rotated_bbox_gdf = gpd.GeoDataFrame(['1'], columns = ['id'], geometry = [min_rotated_rect], crs = input_gdf.crs)

# Save to a new shapefile
rotated_bbox_gdf.to_file("BOUNDING/RO_bbox.shp")

# End of Python Script
print("TASK COMPLETED SUCCESSFULLY")
