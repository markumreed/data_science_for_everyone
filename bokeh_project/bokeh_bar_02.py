from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, sources
from bokeh.palettes import Spectral3
import random

fruits = ['Apples', 'Pears', 'Kiwis', 'Plums', 'Bananas','Strawberries']
year = ["2019", "2020", "2021"]
count_2019 = random.sample(range(1,10), len(fruits))
count_2020 = random.sample(range(1,10), len(fruits)) 
count_2021 = random.sample(range(1,10), len(fruits)) 

data = {"fruits":fruits, '2019':count_2019, '2020':count_2020, '2021':count_2021}
source=ColumnDataSource(data=data)

p = figure(x_range=fruits, plot_height=250, title="Fruit Counts by Year", 
toolbar_location=None, tools="hover", tooltips="$name @fruits: @$name")

p.vbar_stack(year, x="fruits", width=0.95, color=Spectral3, source=data, legend_label=year)

p.y_range.start=0
p.x_range.range_padding = 0.1


show(p)
