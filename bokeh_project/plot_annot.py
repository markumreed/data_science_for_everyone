from bokeh.plotting import figure, show

# prepare some data
x = [1, 2, 3, 4, 5]
y1 = [5, 4, 8, 3, 6]
y2 = [2, 6, 4, 5, 1]
y3 = [1, 2, 4, 6, 1]

p = figure(title="Legend Example")

l = p.line(x, y1, legend_label="Line", line_color="red", line_width=2)
# c = p.circle(x, y2, legend_label="Circle", fill_color="blue", fill_alpha=0.5, size=75)

# display legend in top left corner
p.legend.location = "top_left"

# Add Legend Title
p.legend.title = "My Legend Title"

# Change legend Appearance
p.legend.label_text_font="times"
p.legend.label_text_font_style="bold"
p.legend.label_text_color = "navy"

# Change border and background of legend
p.legend.border_line_width=3
p.legend.border_line_color="navy"
p.legend.border_line_alpha=0.9
p.legend.background_fill_color="yellow"
p.legend.background_fill_alpha=0.2

show(p)