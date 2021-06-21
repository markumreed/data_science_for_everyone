from bokeh.plotting import figure, show
from bokeh.models import BoxAnnotation

import random

# Generate Random data
x = list(range(0, 51))
y = random.sample(range(0,100), 51)

# Create Plot
p = figure(title = "Box annotation example")

l = p.line(x, y, line_color="blue", line_width = 2)

# Add Box Annot
low_box = BoxAnnotation(top=20, fill_alpha=0.1, fill_color="red")
high_box = BoxAnnotation(bottom=80, fill_alpha=0.1, fill_color="red")
mid_box = BoxAnnotation(top=80, bottom=20, fill_alpha=0.1, fill_color="blue")
# Add boxes to figure
p.add_layout(low_box)
p.add_layout(high_box)
p.add_layout(mid_box)


show(p)