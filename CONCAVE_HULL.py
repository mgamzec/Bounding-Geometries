'''
THE GOAL OF THIS PYTHON SCRIPT IS TO EXTRACT THE CONCAVE HULL OUT OF AN INPUT POLYGON SHAPEFILE
'''

import alphashape
import geopandas as gpd
from shapely.geometry import MultiPolygon, Polygon
from geopandas import GeoSeries

# Load shapefile
input_filename = 'pincodebndry.shp'  # Your input shapefile
gdf = gpd.read_file(input_filename)

# Ensure it's in the correct format (GeoDataFrame)
if not isinstance(gdf, gpd.GeoDataFrame):
    gdf = gpd.GeoDataFrame(gdf)

# Extract the exterior points from the polygon geometries
points = []
for geometry in gdf.geometry:
    if isinstance(geometry, Polygon):
        points.extend(geometry.exterior.coords)
    elif isinstance(geometry, MultiPolygon):
        for polygon in geometry.geoms:
            points.extend(polygon.exterior.coords)

# Remove potential invalid values
points = [point for point in points if all(val is not None for val in point)]

# Generate the concave hull
alpha = 25.0  # Try with a fixed alpha value
hull = alphashape.alphashape(points, alpha)

# Create a GeoDataFrame from the hull
hull_gdf = gpd.GeoDataFrame(geometry=GeoSeries(hull))

# Save the hull to a new shapefile
output_filename = 'BOUNDING/CONCAVE_HULL_7.shp'  # Your output shapefile
hull_gdf.to_file(output_filename)

# End of Python Script
print("TASK COMPLETED SUCCESSFULLY")
