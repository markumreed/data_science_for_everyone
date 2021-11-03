from bokeh.plotting import figure, curdoc 
from bokeh.driving import linear 
import random

p = figure(plot_width=800, plot_height=400)
# Allows for following new data
p.x_range.follow = "end"
p.x_range.follow_interval = 20
p.x_range.range_padding = 0
line1 = p.line([],[], color="firebrick", line_width=3)
line2 = p.line([],[], color="navy", line_width=3)

ds1 = line1.data_source
ds2 = line2.data_source

@linear()
def update(step):
	ds1.data['x'].append(step) # Time with no formatting
	ds1.data['y'].append(random.randint(0,100)) # Stock price
	ds2.data['x'].append(step)
	ds2.data['y'].append(random.randint(0, 100))
	ds1.trigger('data', ds1.data, ds1.data)
	ds2.trigger('data', ds2.data, ds2.data)

curdoc().add_root(p)
curdoc().add_periodic_callback(update, 500)