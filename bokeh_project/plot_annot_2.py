from bokeh.plotting import figure, show

x = [1,2,3,4,5]
y = [6,5,4,8,3]

p = figure(title="Main Headline Example")

p.line(x, y, legend_label="Line", line_width=2)


# Change headline location to the left
p.title_location = "left"

# Change Headline Text
p.title.text = "HERE IS THE CHANGED TEXT"

# Style
p.title.text_font_size = "30px"
p.title.align = "right"
p.title.background_fill_color="red"
p.title.text_color="navy"
show(p)