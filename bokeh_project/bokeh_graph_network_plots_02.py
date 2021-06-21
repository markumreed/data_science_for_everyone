from bokeh.plotting import figure, show, from_networkx
from bokeh.models import Range1d, Plot, Circle, HoverTool, MultiLine
from bokeh.models.graphs import NodesAndLinkedEdges
import networkx as nx

G = nx.gnm_random_graph(15, 30)

p = Plot(x_range=Range1d(-2,2), y_range=Range1d(-2,2))
g = from_networkx(G, nx.spring_layout, scale=1.8, center=(0,0))
p.renderers.append(g)

g.node_renderer.glyph = Circle(size=20, fill_color="navy") # Nodes
g.edge_renderer.glyph = MultiLine(line_color="lightblue", line_alpha=0.8, line_width=2) # Edges

g.node_renderer.hover_glyph = Circle(size=20, fill_color="firebrick") # Nodes
g.edge_renderer.hover_glyph = MultiLine(line_color="firebrick", line_width=5) # Edges

g.inspection_policy = NodesAndLinkedEdges()
p.add_tools(HoverTool(tooltips=None))

show(p)
