import networkx as nx

from bokeh.plotting import figure, show, from_networkx
from bokeh.models import BoxZoomTool, Circle, HoverTool, MultiLine, Plot, Range1d, ResetTool
from bokeh.palettes import Spectral4

G = nx.karate_club_graph()
SAME_CLUB_COLOR, DIFFERENT_CLUB_COLOR = "navy", "red"
edge_attr = dict()

for start_node, end_node, _ in G.edges(data=True):
    edge_color = SAME_CLUB_COLOR if G.nodes[start_node]['club'] == G.nodes[end_node]['club'] else DIFFERENT_CLUB_COLOR
    edge_attr[(start_node, end_node)] = edge_color

nx.set_edge_attributes(G, edge_attr, "edge_color")

p = figure(title="Karate Club Graph with Edge Coloring", x_range=(-1.1,1.1), y_range=(-1.1, 1.1))

node_hover_tool = HoverTool(tooltips=[("index", "@index"), ("Club", "@club")])
p.add_tools(node_hover_tool, BoxZoomTool(), ResetTool())


g = from_networkx(G, nx.spring_layout, scale=1, center=(0,0))
g.node_renderer.glyph = Circle(size=15, fill_color=Spectral4[0])
g.edge_renderer.glyph = MultiLine(line_color="edge_color", line_alpha=0.7, line_width=1)

p.renderers.append(g)

show(p)