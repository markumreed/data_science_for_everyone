from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.sampledata.commits import data as df
from bokeh.transform import jitter

DAYS = ["Sun", "Sat", "Fri", "Thu", "Wed", "Tue", "Mon"]

source = ColumnDataSource(df)

p = figure(plot_width = 800, plot_height=400, y_range=DAYS, x_axis_type="datetime", toolbar_location=None,
tools="", title = "Commits by time of day (US/Central) 2012-2016")
p.circle(x="time", y=jitter('day', width=0.6, range=p.y_range ), source=source, alpha=0.3)

p.xaxis[0].formatter.days = ['%Hh']
p.x_range.range_padding=0
p.ygrid.grid_line_color = None

show(p)