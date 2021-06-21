from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.palettes import Spectral3
from bokeh.transform import factor_cmap
import random

# Generate Random Data
fruits = ['Apples', 'Pears', 'Kiwis', 'Plums', 'Bananas','Strawberries']
years = ["2019", "2020", "2021"]
count_2019 = random.sample(range(1,10), len(fruits))
count_2020 = random.sample(range(1,10), len(fruits)) 
count_2021 = random.sample(range(1,10), len(fruits))

data = {"fruits":fruits, '2019':count_2019, '2020':count_2020, '2021':count_2021}

fruit_year = [(fruit, year) for fruit in fruits for year in years]
counts = sum(zip(data['2019'], data['2020'], data['2021']), ())

df = dict(fruit_year=fruit_year, counts=counts)
source=ColumnDataSource(data=df)

p = figure(x_range=FactorRange(*fruit_year), plot_height=250, title="Fruit Counts by Year",
toolbar_location=None, tools="")

p.vbar(x="fruit_year", top="counts", width=0.9, source=source, 
fill_color = factor_cmap("fruit_year", palette=Spectral3, factors=years, start=1, end=2))

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None

show(p)

