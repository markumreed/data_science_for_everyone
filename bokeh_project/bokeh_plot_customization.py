from bokeh.io import curdoc
from bokeh.plotting import figure, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]
# Bokeh comes with five built-in themes: caliber, dark_minimal, light_minimal, night_sky, and contrast
# apply theme to current document
curdoc().theme = "contrast"

# create a plot
p = figure(sizing_mode="stretch_width", max_width=500, plot_height=250)

# add a renderer
p.line(x, y)

# show the results
show(p)