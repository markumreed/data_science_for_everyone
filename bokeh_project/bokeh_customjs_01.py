from bokeh.plotting import figure, show
from bokeh.models import TapTool, CustomJS, ColumnDataSource

x = list(range(11))
y = x

callback = CustomJS(code="alert('You tapped a point on the graph!')")
tap = TapTool(callback=callback)

p = figure(plot_width=500, plot_height=500, tools=[tap])
p.circle(x=x, y=y, size=10)

show(p)