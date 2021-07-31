from bokeh.models import ColumnDataSource, CustomJS, HoverTool
from bokeh.plotting import figure, show 

# Data
x = [2,3,5,6,9,7]
y = [6,5,3,8,7,5]

# Network graph
edges = {
	0: [1,2],
	1: [0,3,4],
	2: [0,5],
	3: [1,4],
	4: [1,3],
	5: [2,3,4]
}

# Create figure
p = figure(plot_width=500, plot_height=500, tools="",toolbar_location=None, title="Hove over nodes")

source = ColumnDataSource(dict(x0 = [], y0=[], x1=[],y1=[] ))

sr = p.segment(x0='x0',y0='y0',x1='x1',y1='y1', color="firebrick", alpha=0.5, line_width=2, source=source)
cr = p.circle(x, y, color="firebrick", size=30, alpha=0.4, hover_color="navy", hover_alpha=1.0)

js_code = """
const edges = %s;
const data = {'x0':[], 'y0':[], 'x1':[], 'y1':[]};
const ind = cb_data.index.indices;
for (var i = 0; i < ind.length; i++){
	const start = ind[i]
	for (var j = 0; j < edges[start].length; j++){
		const end = edges[start][j]
		data['x0'].push(circle.data.x[start])
		data['y0'].push(circle.data.y[start])
		data['x1'].push(circle.data.x[end])
		data['y1'].push(circle.data.y[end])
	}
}
segment.data = data
""" % edges

cb = CustomJS(args={'circle':cr.data_source, 'segment':sr.data_source},code=js_code)
p.add_tools(HoverTool(tooltips=None, callback=cb, renderers=[cr]))

show(p)