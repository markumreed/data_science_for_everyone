from bokeh.layouts import grid, row, column
from bokeh.plotting import figure, show

x = list(range(11))
y0 = x
y1 = [10 - i for i in x]
y2 = [abs(i-3) for i in x]
y3 = [10 + i for i in x] 

# create 3 plots and render
p1 = figure(plot_width=250, plot_height=250)
p1.circle(x, y0, size=10)

p2 = figure(plot_width=250, plot_height=250)
p2.triangle(x, y1, size=10)

p3 = figure(plot_width=250, plot_height=250)
p3.square(x, y2, size=10)

p4 = figure(plot_width=250, plot_height=250)
p4.square(x, y3, size=10)

show(grid([p1, p2, p3, p4], ncols=2))




