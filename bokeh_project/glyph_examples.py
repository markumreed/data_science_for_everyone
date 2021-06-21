# Basic Imports
from bokeh.plotting import figure, show

# prepare some data
x = [1, 2, 3, 4, 5]
y1 = [5, 4, 8, 3, 6]
y2 = [2, 6, 4, 5, 1]
y3 = [1, 2, 4, 6, 1]

# Create Figure
# p = figure(title="Bokeh Glyph Examples", x_axis_label="x", y_axis_label="y")

# Add Renderers/Glyphs
# p.line(x, y1, legend_label="Blue Line", line_color="blue", line_width=2)
# p.vbar(x=x, top=y3, legend_label="Bar", width=0.5, bottom=0, color="red")
# p.circle(x, y2, legend_label="Circle", line_color="yellow", size=10)

# Circle Customization
p = figure(title="Glyph Properties", x_axis_label="x", y_axis_label="y")

circ = p.circle(x, y2, legend_label="Custom Circles", fill_color="blue", 
line_color="red", fill_alpha=0.5, size=90)

g = circ.glyph
g.fill_color="red"
show(p)