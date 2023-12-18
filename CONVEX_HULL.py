'''
THE GOAL OF THIS PYTHON SCRIPT IS TO EXTRACT THE CONVEX HULL OUT OF AN INPUT POLYGON SHAPEFILE
'''

import geopandas as gpd

# Load the input shapefile
input_gdf = gpd.read_file("pincodebndry.shp")

# Merge all geometries in the GeoDataFrame into one
union_geometry = input_gdf.unary_union

# Compute the convex hull of the union
convex_hull = union_geometry.convex_hull

# Create a new GeoDataFrame with the convex hull
# Use 'id' as column name and '1' as its value
convex_hull_gdf = gpd.GeoDataFrame(['1'], columns=['id'], geometry=[convex_hull], crs=input_gdf.crs)

# Save to a new shapefile
convex_hull_gdf.to_file("BOUNDING/convex_hull_2.shp")

# End of Python Script
print("TASK COMPLETED SUCCESSFULLY")
