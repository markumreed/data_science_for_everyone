from bokeh.plotting import figure, show
from bokeh.layouts import column
from bokeh.models import CustomJS, ColumnDataSource, Slider, sources

x = [x*.005 for x in range(0,201)]
source = ColumnDataSource(data=dict(x=x,y=x))

p = figure(plot_width=500, plot_height=500)
p.line('x', 'y', source=source, line_width=4, line_alpha=0.6)

slider = Slider(start=0.1, end=6, value=1, step=0.1, title="Power")


js_code="""
    var data = source.data;
    var f = slider.value;
    var x = data['x']
    var y = data['y']
    for (var i = 0; i < x.length; i++) {
        y[i] = Math.pow(x[i], f)
    }
    // Mutate source.data in-place
    source.change.emit();
"""

update_curve = CustomJS(args=dict(source=source, slider=slider), code=js_code)

slider.js_on_change('value', update_curve)

show(column(slider, p))