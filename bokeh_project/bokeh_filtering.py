from bokeh.layouts import gridplot
from bokeh.models import CDSView, ColumnDataSource, IndexFilter
from bokeh.plotting import figure, show

# Create Data
data = dict(x=[1,2,3,4,5], y=[5,4,3,2,1])
source = ColumnDataSource(data=data)

# Create a view using an index filter
view = CDSView(source=source, filters=[IndexFilter([0,2,4])])

# setup tools
tools = ["box_select", "hover", "reset"]

# Create figures
p = figure(plot_width=500, plot_height=500, tools=tools)
p.circle(x="x", y="y", size=0, hover_color="red", source=source)

# create 2nd plot
p_filtered = figure(plot_width=500, plot_height=500, tools=tools)
p_filtered.circle(x="x", y="y", size=30, hover_color="red", source=source, view=view)

# show
show(gridplot([[p,p_filtered]]))
