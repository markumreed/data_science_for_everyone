from bokeh.plotting import figure, show
from bokeh.models import WMTSTileSource

USA = x_range, y_range = ((-13884029, -7453304), (2698291,6455972))

p = figure(tools="pan, wheel_zoom", x_range=x_range, y_range=y_range, 
x_axis_type="mercator", y_axis_type="mercator")

url = "http://a.basemaps.cartocdn.com/rastertiles/voyager/{Z}/{X}/{Y}.png"
attribution = "Tiles by Carto, under CC BY 3.0. Data by OSM, under ODbL"

p.add_tile(WMTSTileSource(url=url, attribution=attribution))

show(p)



