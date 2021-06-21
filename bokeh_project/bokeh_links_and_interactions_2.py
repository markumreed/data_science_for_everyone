# linked brushing
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot

x = list(range(-20, 20))
y0, y1 = [abs(a) for a in x], [b**2 for b in x]

data = dict(x=x, y0=y0, y1=y1)

source = ColumnDataSource(data = data)

TOOLS = "box_select, lasso_select, help"

options = dict(tools=TOOLS, plot_width=500, plot_height=500)
# create figures

f1 = figure(**options)
f1.circle('x', 'y0', source=source)

f2 = figure(**options)
f2.triangle('x', 'y1', source=source)

figures = [f1, f2]

p = gridplot([figures])

show(p)

#