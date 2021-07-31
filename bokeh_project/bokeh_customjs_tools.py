from bokeh.events import SelectionGeometry
from bokeh.models import ColumnDataSource, CustomJS, Rect
from bokeh.plotting import figure, show 

# Rect
source = ColumnDataSource(data=dict(x=[], y=[], width=[],height=[]))

js_code = """
const geometry = cb_obj['geometry'];
const data = source.data

// Calculation of Rect Attributes
const width = geometry['x1'] - geometry['x0']
const height = geometry['y1'] - geometry['y0']
const x = geometry['x0'] + width / 2;
const y = geometry['y0'] + height / 2;

// Update Data

data['x'].push(x);
data['y'].push(y);
data['width'].push(width);
data['height'].push(height);

source.change.emit()
"""

cb = CustomJS(args=dict(source=source), code = js_code)

p = figure(plot_width=500, plot_height=500, tools="box_select,reset",
	title="Make Selection Below", x_range=(0,1),y_range=(0,1))

rect = Rect(x="x",y="y", width="width", height="height", fill_alpha=0.4, fill_color="#B22222")

p.add_glyph(source, rect, 
	selection_glyph=rect, nonselection_glyph=rect)

p.js_on_event(SelectionGeometry, cb)

show(p)