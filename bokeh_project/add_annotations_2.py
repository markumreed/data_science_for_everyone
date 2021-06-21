from bokeh.models.layouts import Box
from bokeh.plotting import figure, show
from bokeh.models.annotations import Span 
import numpy as np

x = np.linspace(0, 20, 200)
y = np.sin(x)

p = figure(y_range=(-2, 2))
p.line(x, y)

# upper = Span(location=1, dimension="width", line_color="navy", line_width=4)
# p.add_layout(upper)

# lower = Span(location=-1, dimension="width", line_color="firebrick", line_width=4)
# p.add_layout(lower)
# show(p)

# from bokeh.models.annotations import BoxAnnotation

# upper = BoxAnnotation(bottom=1, fill_alpha=0.1, fill_color="navy")
# p.add_layout(upper)

# lower = BoxAnnotation(top=-1, fill_alpha=0.1, fill_color="firebrick")
# p.add_layout(lower)

# center = BoxAnnotation(top=0.6, bottom=-0.3, right=12, left=7, fill_alpha=0.1, fill_color="olive")
# p.add_layout(center)
# show(p)

# from bokeh.models.annotations import Label
# p = figure(x_range=(0,10), y_range=(0,10))
# p.circle([2,5,8], [4,7,6], color="navy", size=10)

# label = Label(x=5, y=7, x_offset=12, text="Point #2", text_baseline="middle")
# p.add_layout(label)

# label2 = Label(x=2, y=4, x_offset=12, text="Point #1", text_baseline="middle")
# p.add_layout(label2)

# show(p)

# from bokeh.models import ColumnDataSource, LabelSet
# source = ColumnDataSource(
#     data=dict(
#         temp=[155, 183, 164, 170, 163],
#         pressure = [156, 200, 190, 151, 300],
#         names = list("ABCDE")
#     )
# )

# p=figure(x_range=(150, 190))
# p.circle(x="temp", y="pressure", size=8, source=source)
# p.xaxis.axis_label = "Temp"
# p.yaxis.axis_label ="Pressure"

# label = LabelSet(x="temp", y="pressure", text="names", level="glyph",
# x_offset=5, y_offset=5, source=source, render_mode="canvas")

# p.add_layout(label)

# show(p)

from bokeh.models.annotations import Arrow
from bokeh.models.arrow_heads import OpenHead, NormalHead, VeeHead

x = [0, 1, 0.5]
y = [0, 0, 0.7]

p = figure(plot_width=600, plot_height=600)
p.circle(x=x, y=y, radius=0.1, color=["navy", "olive", "firebrick"], fill_alpha=0.1)

# Make some Arrows
arrow_1 = Arrow(end=OpenHead(line_color="navy", line_width=4), x_start=0, y_start=0, x_end=1, y_end=0)
p.add_layout(arrow_1)

arrow_2 = Arrow(end=NormalHead(fill_color="olive"), x_start=1, y_start=0, x_end=0.5, y_end=0.7)
p.add_layout(arrow_2)

arrow_3 = Arrow(end=VeeHead(size=40), line_color="firebrick", x_start=0.5, y_start=0.7, x_end=0, y_end=0)
p.add_layout(arrow_3)
show(p)



