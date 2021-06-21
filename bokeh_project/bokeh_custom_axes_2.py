from bokeh.plotting import figure, show
from bokeh.models import NumeralTickFormatter

x =[1,2,3,4,5]
y =[2,3,4,3,5]

p = figure(
    title="Tick formatter",
    sizing_mode="stretch_width",
    max_width=800,
    plot_height=250,
)
# format axes ticks
p.yaxis[0].formatter = NumeralTickFormatter(format="$0.00")

# glyph
p.circle(x, y, size=5)
p.line(x, y, color = "red", line_width=1)

show(p)