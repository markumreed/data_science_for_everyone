from bokeh.plotting import figure, show
# import bokeh.sampledata
# bokeh.sampledata.download()
import pandas as pd
from bokeh.sampledata.iris import flowers as df

p = figure(plot_width=500, plot_height=500)
p.circle("petal_length", "petal_width", source=df)
show(p)




