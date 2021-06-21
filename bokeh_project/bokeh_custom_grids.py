from bokeh.plotting import figure, show

x = [1,2,3,4,5]
y = [4,5,5,8,1]

# create plot
p = figure(
    title="Background Colors",
    sizing_mode="stretch_width",
    max_width=900,
    plot_height=250,
)

# Renderer
p.line(x, y, line_color="red", line_width=3)

# change backgroun fill colors
# p.background_fill_color = (50, 168, 82)
# p.border_fill_color = (217, 46, 20)
p.outline_line_color = (217, 17, 217)

# # add bands to y-grid
# p.ygrid.band_fill_color = "blue"
# p.ygrid.band_fill_alpha = 0.1

# # define vertical bounds
# p.xgrid.bounds = (2,4)

# # Change x-grid
# p.xgrid.grid_line_color = "green"

# # Change y-grid
# p.ygrid.grid_line_alpha = 0.8
# p.ygrid.grid_line_dash = [6, 4]
# p.ygrid.grid_line_color = "navy"

# Show
show(p)