'''
THE GOAL OF THIS PYTHON SCRIPT IS TO EXTRACT A DELAUNAY TRIANGULATION OUT OF AN INPUT POLYGON SHAPEFILE
'''

import geopandas as gpd
from shapely.geometry import Polygon
from scipy.spatial import Delaunay
import numpy as np

# Load the shapefile
gdf = gpd.read_file("pincodebndry.shp")

# Combine all the polygons into a single MultiPolygon
multipolygon = gdf.unary_union

# Get the coordinates of the multipolygon
coords = np.array(multipolygon.exterior.coords)

# Perform Delaunay triangulation
tri = Delaunay(coords)

# Convert the triangles to Shapely polygons
triangles = [Polygon(coords[vertices]) for vertices in tri.simplices]

# Create a new GeoDataFrame to save the triangles
tri_gdf = gpd.GeoDataFrame(geometry = triangles)

# Save the triangles to a new shapefile
tri_gdf.to_file("BOUNDING/TRIANGULATION.shp")

# End of Python Script
print("TASK COMPLETED SUCCESSFULLY")
