# imports
from bokeh.plotting import figure, show

# prepare some data
x = [1, 2, 3, 4, 5]
y1 = [5, 4, 8, 3, 6]
y2 = [2, 6, 4, 5, 1]
y3 = [1, 2, 4, 3, 1]


# Create figure/plot with title and axis labels
p = figure(title="A Simple Multi-Line Plot",  x_axis_label="x", y_axis_label="y")

# Add line graph, Renderers
p.line(x, y1, legend_label="Blue Line", line_color="blue", line_width=2)
p.line(x, y2, legend_label="Red Line", line_color="red", line_width=2)
p.line(x, y3, legend_label="Green Line", line_color="green", line_width=2)
# Show the results

show(p)