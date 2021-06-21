from bokeh.plotting import figure, output_file, save
from bokeh.io import export_svg

x = list(range(11))
y = [abs(10 - i) for i in x]

# output to static HTML file
output_file(filename="HERE IS MY NEW FILE.html", title="HTML FILE")

p = figure(sizing_mode="stretch_width", max_width=500, max_height=250)

p.circle(x, y, fill_color="blue", size=10)

export_svg(p, filename="ANOTHER PLOT.svg")