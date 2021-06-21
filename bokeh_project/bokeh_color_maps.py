from bokeh.plotting import figure, show
from bokeh.palettes import Viridis, Turbo256
from bokeh.transform import linear_cmap

# Some Palettes are Dictionaries, Some are Lists

# generate data

x = list(range(-32, 33))
y = [i**2 for i in x]

# Create linear Color map, Expects a list
mapper = linear_cmap(field_name="y", palette=Turbo256, low=min(y), high=max(y))

#Create plot
p = figure(
    plot_width = 800,
    plot_height = 400,
)

p.circle(x, y, color=mapper, size=10)

show(p)