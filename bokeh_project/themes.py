from bokeh.io import curdoc
from bokeh.plotting import figure, show

# prep data
x = [1,2,3,4,5]
y = [2,3,5,5,4]

# apply theme
# caliber, dark_minimal, light_minimal, night_sky, contrast
curdoc().theme = "contrast"

# create plot
p = figure(sizing_mode = "stretch_width", max_width = 500, plot_height=250)

# add renderer
p.line(x, y)

#show
show(p)