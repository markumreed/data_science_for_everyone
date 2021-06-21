from bokeh.models.annotations import Tooltip
from bokeh.plotting import figure, show
import pandas as pd
from math import pi
from bokeh.palettes import Category20c
from bokeh.transform import cumsum

x = dict(US = 158,UK = 94, Japan = 89, China = 62,Germany = 44,India = 43,

)

data = pd.Series(x).reset_index(name="value").rename(columns={"index":"country"})
data['color'] = Category20c[len(x)]

# represent each value as an angle
# Creating pie chart
data['angle'] = data['value'] / data['value'].sum() * 2*pi

# create figure
p = figure(plot_height = 400, title="Country Pie Chart", toolbar_location=None,
tools="hover", tooltips="@country: @value")

p.wedge(x=0, y=1, radius =0.4,
# user cumsum
start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
line_color="white", fill_color="color", legend_field="country", source=data
 )

p.axis.axis_label=None
p.axis.visible = False
p.grid.grid_line_color=None

show(p)