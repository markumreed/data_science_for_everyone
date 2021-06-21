from bokeh.plotting import figure, show
from bokeh.models import HoverTool, ColumnDataSource

data = dict(
    x=[1,2,3,4,5],
    y=[2,5,7,3,9],
    letter = list('ABCDE')
)

source = ColumnDataSource(data=data)
hover = HoverTool(
    tooltips=[
        ('Index', "$index"),
        ("(x,y)", "($x, $y)"),
        ("Letter", "@letter")
    ]
)

p = figure(plot_width=500, plot_height=500, tools=[hover], title="Hover Over the Scatter Plot")
p.circle('x', 'y', source=source, size=30)

show(p)