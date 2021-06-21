from bokeh.plotting import figure, show
from bokeh.models.tools import HoverTool

x = [1,2,3,4,5]
y = [3,4,5,5,2]

p = figure(
    title="Toolbar Customization",
    sizing_mode = "stretch_width",
    tools = [HoverTool()],
    tooltips = "Data point @x has the value @y",
    max_width = 400,
    plot_height = 250,
)
# Toolbar
# p.toolbar.autohide = True
# p.toolbar.logo = None
# p.add_tools(PanTool(dimensions="width"))

p.circle(x,y, size=10)
p.line(x,y)

show(p)