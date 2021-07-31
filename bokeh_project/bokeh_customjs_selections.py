from random import random
from bokeh.layouts import row 
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.plotting import figure, show 

x = [random() for x in range(1000)]
y = [random() for y in range(1000)]

s1 = ColumnDataSource(data=dict(x=x, y=y))
p1 = figure(plot_width = 500, plot_height = 500, tools="lasso_select", title="Make Your Selection Here")
p1.circle('x', 'y', source=s1, alpha=0.7)

s2 = ColumnDataSource(data=dict(x=[], y=[]))
p2 = figure(plot_width=500, plot_height=500, x_range=(0,1), y_range=(0,1),
tools="save", title="Look Over Here")
p2.circle('x','y', source=s2, alpha=0.7)

## Callback
s1.selected.js_on_change('indices', CustomJS(args=dict(s1=s1,s2=s2),
code="""
var inds = cb_obj.indices;
var d1 = s1.data;
var d2 = s2.data;
d2['x'] = []
d2['y'] = []

for (var i = 0; i < inds.length; i++){
	d2['x'].push(d1['x'][inds[i]])
	d2['y'].push(d1['y'][inds[i]])
}

s2.change.emit(); // push data to python 
"""
))




# Layout
layout = row(p1, p2)
show(layout)

