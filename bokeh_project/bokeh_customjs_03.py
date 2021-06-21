# Data Selection Example

from random import random
from bokeh.plotting import figure, show
from bokeh.models import CustomJS, ColumnDataSource

x = [random() for x in range(500)]
y = [random() for y in range(500)]
color = ['navy'] * len(x)

d1 = ColumnDataSource(data=dict(x=x, y=y, color=color))
p = figure(plot_width=500, plot_height = 500, tools="lasso_select", title="Select Here")
p.circle('x', 'y', color='color', size=10, alpha=0.4, source=d1, 
selection_color="firebrick", selection_alpha=0.3)

d2 = ColumnDataSource(data=dict(xm=[0,1], ym=[0.5, 0.5]))
p.line(x="xm", y="ym", color="orange", line_width=5, alpha=0.6, source=d2)

js_code = """
    var inds = d1.selected.indices;
    if (inds.length == 0) {
        return;
    }
    var ym=0
    for (var i = 0; i < inds.length; i++) {
        ym += d1.data.y[inds[i]]
    }
    ym /= inds.length
    d2.data.ym = [ym, ym]

    // Since we have change/mutated the source data we much emit data
    d2.change.emit();
"""

callback = CustomJS(args=dict(d1=d1, d2=d2), code=js_code)

d1.selected.js_on_change("indices", callback)

show(p)