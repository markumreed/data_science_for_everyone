from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool, LogColorMapper
import geopandas as gpd
import pysal as ps


grid_fp = "data/travel_times.shp"
point_fp = "data/addresses.shp"
metro_fp = "data/metro.shp"

grid = gpd.read_file(grid_fp)
points = gpd.read_file(point_fp)
metro = gpd.read_file(metro_fp)

print(grid.crs)
points['geometry'] = points['geometry'].to_crs(crs=CRS)
metro['geometry'] = metro['geometry'].to_crs(crs=CRS)

def getPolyCoords(row, geom = 'geometry', coord_type = ''):
	ext = row[geom].exterior

	if coord_type == 'x':
		return list(ext.coords.xy[0])
	elif coord_type == 'y':
		return list(ext.coords.xy[1])

def parser(df):
	df['x'] = df.apply(getPolyCoords, geom='geometry', coord_type='x', axis=1)
	df['y'] = df.apply(getPolyCoords, geom='geometry', coord_type='y', axis=1)
	return df['x'], df['y']

grid['x'], grid['y'] = parser(grid)
metro['x'], metro['y'] = parser(metro)
points['x'], points['y'] = parser(points)

# Replace No Data values (-1) with large number (999)
grid = grid.replace(-1, 999)

# Classify our travel times into 5 minute classes until 200 minutes
# Create a list of values where minumum value is 5, maximum value is 200 and step is 5.
breaks = [x for x in range(5, 200, 5)]

# Initialize the classifier and apply it
classifier = ps.User_Defined.make(bins=breaks)
pt_classif = data[['pt_r_tt']].apply(classifier)

# Rename the classified column
pt_classif.columns = ['pt_r_tt_ud']

# Join it back to the grid layer
grid = grid.join(pt_classif)

print(grid.head())


