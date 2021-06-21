from bokeh.plotting import figure, show, from_networkx
from bokeh.models import Range1d, Plot, HoverTool
from bokeh.palettes import Category20_20

import networkx as nx

# NetworkX
G = nx.desargues_graph()

# Plot figure 
p = Plot(x_range=Range1d(-2, 2), y_range=Range1d(-2, 2))

# Creating a bokeh graph
g = from_networkx(G, nx.spring_layout, scale = 1.8, center=(0,0))
p.renderers.append(g)

# Add Data
g.node_renderer.data_source.data['person'] = list(range(len(G)))
g.node_renderer.data_source.data["colors"] = Category20_20

# Setup default node as circle
g.node_renderer.glyph.update(size=15, fill_color="colors")

# Set edges (connections)
g.edge_renderer.glyph.line_dash = [2,2]

p.add_tools(HoverTool(tooltips="Person ID: @person"))

show(p)


