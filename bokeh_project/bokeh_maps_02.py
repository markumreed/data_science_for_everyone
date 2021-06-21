from bokeh.plotting import figure, show
from bokeh.models import WMTSTileSource
import pandas as pd
import numpy as np

def web_mercator(df, lon="lon", lat="lat"):
    # Convert dec lon/lat to Web Mercator format
    k = 6378137
    df["x"] = df[lon] * (k * np.pi/180.0)
    df["y"] = np.log(np.tan((90 + df[lat]) * np.pi / 360)) * k
    return df

data = dict(
    name = ["Dallas", "Chicago", "NYC", "LA"], 
    lat=[32.78, 41.90, 40.7128, 33.93], 
    lon = [-96.81, -87.65, -74.01, -118.40]
    )
df = pd.DataFrame(data) # DataFrame
map_df = web_mercator(df)
# print(map_df.head())
USA = x_range, y_range = ((-13884029, -7453304), (2698291,6455972))

p = figure(tools="pan, wheel_zoom", x_range=x_range, y_range=y_range, 
x_axis_type="mercator", y_axis_type="mercator")

url = "http://a.basemaps.cartocdn.com/rastertiles/voyager/{Z}/{X}/{Y}.png"
attribution = "Tiles by Carto, under CC BY 3.0. Data by OSM, under ODbL"

p.add_tile(WMTSTileSource(url=url, attribution=attribution))
p.circle(x=df['x'], y=df['y'], fill_color="firebrick", size=15)

show(p)