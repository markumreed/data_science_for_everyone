from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, sources
from bokeh.palettes import GnBu3, OrRd3
import random

fruits = ['Apples', 'Pears', 'Kiwis', 'Plums', 'Bananas','Strawberries']
year = ["2019", "2020", "2021"]
export_2019 = random.sample(range(1,10), len(fruits))
export_2020 = random.sample(range(1,10), len(fruits)) 
export_2021 = random.sample(range(1,10), len(fruits)) 

import_2019 = random.sample(range(-10,-1), len(fruits))
import_2020 = random.sample(range(-10,-1), len(fruits)) 
import_2021 = random.sample(range(-10,-1), len(fruits)) 


exports = {"fruits":fruits, '2019':export_2019, '2020':export_2020, '2021':export_2021}
imports = {"fruits":fruits, '2019':import_2019, '2020':import_2020, '2021':import_2021}

p = figure(y_range=fruits, plot_height=250, x_range=(-40, 30), 
title="Import/Export for Fruits", toolbar_location=None)

p.hbar_stack(year, y="fruits", height=0.9, color=GnBu3, source=ColumnDataSource(exports),
legend_label=["%s exports" % x for x in year])
p.hbar_stack(year, y="fruits", height=0.9, color=OrRd3, source=ColumnDataSource(imports),
legend_label=["%s imports" % x for x in year])

p.y_range.range_padding = 0.1
p.ygrid.grid_line_color = None

p.legend.location = "top_left"

show(p)
