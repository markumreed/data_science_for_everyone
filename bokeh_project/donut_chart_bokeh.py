
from math import pi
import numpy as np
from bokeh.io import output_file, show
from bokeh.palettes import Category10
from bokeh.plotting import figure
from bokeh.transform import cumsum
from bokeh.models import Legend, HoverTool, LegendItem, LabelSet, ColumnDataSource

output_file("pie.html")

value = [10,20,30,40]*5

data = {
	'name': ["A", "B","C","D"]*5,
	'value': value,
	'angle': [v/sum(value)*2*pi for v in value],
	'cumulative_angle':[(sum(value[0:i+1])- (item/2))/sum(value)*2*pi for i,item in enumerate(value)],
	'percentage': [d/sum(value)*100 for d in value],
	'color': Category10[5][1:]*5
	}

data['label'] = ["{:.0f}%".format(p) for p in data['percentage']]
data['cos'] = np.cos(data['cumulative_angle'])*0.3
data['sin'] = np.sin(data['cumulative_angle'])*0.3
source = ColumnDataSource(data=data)

TOOLTIPS = [
("Value", "@value"),
("Percentage", "@percentage{0.2f}%")
]

p = figure(plot_height=600,plot_width=600,x_range=(-1,1), y_range=(-1,1), tools='hover',

tooltips=TOOLTIPS, title="My Donut Chart", toolbar_location=None)

r = p.annular_wedge(x=0, y=0, inner_radius=0.2, outer_radius=0.4,

start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),

line_color="white", fill_color='color', fill_alpha=1, source=source)

legend = Legend(items=[LegendItem(label=dict(field="name"), renderers=[r])], location=(0, 80))

p.add_layout(legend, 'right')

labels = LabelSet(x='cos', y='sin', text="label", y_offset=0,

text_font_size="6pt", text_color="black",

source=source, text_align='center')

p.add_layout(labels)

p.axis.axis_label=None

p.axis.visible=False

p.grid.grid_line_color = None

p.outline_line_color = None

show(p)
