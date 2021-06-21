from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
fruits = ['Apples', 'Pears', 'Kiwis', 'Plums', 'Bananas','Strawberries']
counts = [5, 3, 6, 2, 7, 10]
data = dict(fruits=fruits, counts=counts, color = Spectral6)

source = ColumnDataSource(data=data)



p = figure(x_range=fruits, y_range=(0,14), plot_height=250, title="Counting Fruits", toolbar_location=None, tools="")

p.vbar(x='fruits', top='counts', width=0.95, color='color', legend_field="fruits", source=source)
p.y_range.start = 0
p.xgrid.grid_line_color=None

# Legend
p.legend.orientation = "horizontal"
p.legend.location = "top_center"



show(p)
