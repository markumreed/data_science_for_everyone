from bokeh.plotting import figure, show

# create data
x = [1,2,3,4,5]
y = [3,4,4,5,1]

# create new plot with specific sizes
p = figure(
    title="Plot Resizing",
    sizing_mode ="stretch_width",
    plot_height = 250,
    x_axis_label="x",
    y_axis_label="y",
)
# # change plot size
# p.plot_width = 450
# p.plot_height = 150

# scatter plot / circle
p.circle(x, y, fill_color="blue", size=20)

# show
show(p)
