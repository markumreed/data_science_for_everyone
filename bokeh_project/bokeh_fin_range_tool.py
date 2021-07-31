import yfinance as yf
import pandas as pd
import numpy as np

from bokeh.plotting import figure, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, RangeTool

# Data
data = yf.download('SPY')
data.reset_index(inplace=True)

dates = np.array(data["Date"])
# print(data.head())

source = ColumnDataSource(data=data)

p = figure(plot_height=300, plot_width=1000, tools="xpan",
	toolbar_location=None, x_axis_type="datetime", x_axis_location="above",
		x_range=(dates[1500], dates[2500]))
p.line('Date','Adj Close', source=source)
p.yaxis.axis_label = "Price"
select = figure(title="Drag the middle and edges of the Selection Box to Change the Range",
	plot_height=150, plot_width=1000, y_range=p.y_range, x_axis_type="datetime",y_axis_type=None,
	tools="", toolbar_location=None)

range_tool = RangeTool(x_range=p.x_range)
range_tool.overlay.fill_color="navy"
range_tool.overlay.fill_alpha = .2

select.line('Date', 'Adj Close', source=source)
select.ygrid.gird_line_color=None
select.add_tools(range_tool)
select.toolbar.active_multi = range_tool

show(column(p, select))

