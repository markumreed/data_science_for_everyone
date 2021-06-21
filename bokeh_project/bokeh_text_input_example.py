from bokeh.layouts import layout
from bokeh.io import curdoc
from bokeh.models.widgets import AutocompleteInput
from bokeh.models.widgets import (Panel, Tabs, DataTable, TableColumn,
                                  Paragraph, Slider, Div, Button, Select)
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import HoverTool,TapTool

def update_selected(wttr,old,new):
    a_val = autocomp.value
    names = source.data['names']
    ind = [i for i,x in enumerate(names) if x == a_val]
    source.selected={'0d': {'glyph': None, 'indices': []}, '1d': {'indices': ind}, '2d': {}}


data_dict = {'names':['test2','test3','hello','goodbye'],
           'x':[0,1,2,3], 'y':[10,20,30,40]}   
source = ColumnDataSource(data_dict)
autocomp = AutocompleteInput(completions=['test2','test3','hello','goodbye'])
autocomp.on_change('value',update_selected )
fig = figure(plot_width=400,
             plot_height=400,
             x_axis_label='x',
             y_axis_label='y',
             tools=["pan","hover","box_zoom","reset,save"])

fig.scatter('x','y',source=source)
layout = layout([[fig, autocomp]])
curdoc().add_root(layout)