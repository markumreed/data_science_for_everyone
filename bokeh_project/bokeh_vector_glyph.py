import numpy as np
from bokeh.plotting import figure, show

# Generate Data
N = 1000
x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100 

# generate random rgb hex colors wrt y
radius = y / 100 * 2
colors = ["#%02x%02x%02x" % (255, int(round(value * 255 / 100)), 255) for value in y]

# create plot
p = figure(
    title="Vectorized Colors",
    sizing_mode = "stretch_width",
    max_width = 700,
    plot_height = 250,
)

# Renderers
p.circle(x, y, radius = radius, fill_color = colors, fill_alpha=0.5, line_color="lightblue", size=20)

# show
show(p)