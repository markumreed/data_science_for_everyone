from bokeh.models import ColumnDataSource, OpenURL, TapTool, Label, LabelSet
from bokeh.plotting import figure, show

# data
x = [1,2,3,4,5]
y = [2,5,8,2,7]
country = ['China', 'Japan','Germany', 'United_States', 'Canada']
data = dict(x=x, y=y, country=country)
source = ColumnDataSource(data)
p = figure(plot_width=500, plot_height=500, tools="tap", title="Click a Country")
p.circle('x', 'y', size=20, source=source)

labels = LabelSet(x='x',y='y', text='country', x_offset=5, y_offset=5, source=source, render_mode='canvas')

url = "https://en.wikipedia.org/wiki/@country"

taptool = p.select(type=TapTool)
taptool.callback = OpenURL(url=url)

p.add_layout(labels)

show(p)