from bokeh.plotting import figure, show
from bokeh.layouts import gridplot

# Linked Pan

x = list(range(11))
y0, y1, y2 = x, [10-i for i in x], [abs(i-5) for i in x]

options = dict(plot_width=500, plot_height = 500, tools="pan, wheel_zoom" )

# create 2 plots
f1 = figure(**options)
f1.circle(x, y0, size=10, color="firebrick")

# new figure will share both ranges of f1
f2 = figure(x_range=f1.x_range, y_range=f1.y_range, **options)
f2.square(x, y1, size=10, color="navy")

f3 = figure(x_range = f1.x_range, **options)
f3.triangle(x, y2, size=10, color="olive")

figures = [f1, f2, f3]
p = gridplot([figures])

show(p)