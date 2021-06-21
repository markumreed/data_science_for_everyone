from bokeh.plotting import figure, show

# prep data
x = [1,2,3,4,5]
y = [2,4,6,3,2]

# create plot
p = figure(
    title = "Custom Axes",
    sizing_mode = "stretch_width",
    max_width = 700,
    plot_height = 350,
)

# add circle renderer
p.circle(x, y, size = 15)

# change the x-axis
p.xaxis.axis_label = "I'm the X Axis"
p.xaxis.axis_line_width = 4
p.xaxis.axis_line_color = "red"

# change y-axis
p.yaxis.axis_label = "AHH, I'm the Y Axis"
p.yaxis.major_label_text_color = "orange"
p.yaxis.major_label_orientation = "vertical"

# Both axes
p.axis.minor_tick_in = -2
p.axis.minor_tick_out = 5

# show
show(p)