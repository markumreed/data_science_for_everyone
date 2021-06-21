from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DatetimeTickFormatter, Select
from bokeh.layouts import layout
from bokeh.plotting import figure
from datetime import datetime
from math import radians # rotate axis ticks
import numpy as np

#create figure
f=figure(x_axis_type='datetime', width=800, height=250)

#genderate data function
def create_value():
    draws = np.random.randint(0, 2, size=200)
    steps = np.where(draws > 0, 1, -1)
    walk = steps.cumsum()
    return walk[-1]

#create ColumnDataSource
source=ColumnDataSource(dict(x=[],y=[]))

#create glyphs
f.circle(x='x',y='y',color='olive',line_color='brown',source=source)
f.line(x='x',y='y',source=source)


#create periodic function
def update():
    new_data=dict(x=[datetime.now()],y=[create_value()])
    source.stream(new_data,rollover=200)
    # print(source.data)
    f.title.text = "Now Streaming %s Data" % select.value


def update_intermediate(attr, old, new):
    source.data=dict(x=[],y=[])
    update()
date_pattern = ["%Y-%m-%d\n%H:%M:%S"]
f.xaxis.formatter=DatetimeTickFormatter(
seconds=date_pattern,
minsec=date_pattern,
minutes=date_pattern,
hourmin=date_pattern,
hours=date_pattern,
days=date_pattern,
months=date_pattern,
years=date_pattern,
)

f.xaxis.major_label_orientation=radians(80)
f.xaxis.axis_label = "Date"
f.yaxis.axis_label = "Value"

#create Select widget
options=[("stock1","Stock One"),("stock2","Stock Two")]
select=Select(title="Market Name",value="stock1",options=options)
select.on_change("value",update_intermediate)

#add figure to curdoc and configure callback
lay_out=layout([[f],[select]])
curdoc().title = "Streaming Stock Data"
curdoc().theme = 'dark_minimal'
curdoc().add_root(lay_out)
curdoc().add_periodic_callback(update,500)
