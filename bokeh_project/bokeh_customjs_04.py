from bokeh.plotting import figure, show
from bokeh import events
from bokeh.models import CustomJS, Div, Button
from bokeh.layouts import column, layout, row

import numpy as np
x = np.random.random(size=2000) * 100
y = np.random.random(size=2000) * 100

p = figure(plot_width=500, plot_height=500, tools="box_select")
p.circle(x, y, radius=1, fill_alpha=0.6, line_color=None)

div = Div(width=500)
button = Button(label="Click Me!", width=400)
layout = column(button, row(p, div))

# Event with no attributes
js_code_01 = "div.text = 'HELLO THERE!'"
button.js_on_event(events.ButtonClick, CustomJS(args=dict(div=div), code=js_code_01))


js_code_02 = """
    div.text = "<p>You made a selection!</p>" + JSON.stringify(cb_obj.geometry, undefined, 2);
"""
p.js_on_event(events.SelectionGeometry, CustomJS(args=dict(div=div), code=js_code_02))

show(layout)

