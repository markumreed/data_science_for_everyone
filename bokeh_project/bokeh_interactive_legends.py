import pandas as pd

from bokeh.plotting import figure, show
from bokeh.palettes import Spectral4
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT

p = figure(plot_width=800, plot_height=250, x_axis_type="datetime")
p.title.text = "Click on the legend to hide the lines: Stock Plot"

for data, name, color in zip([AAPL, GOOG, IBM, MSFT], ["AAPL", "GOOG", "IBM", "MSFT"], Spectral4):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    p.line(df['date'], df['close'], line_width=2, color=color, alpha=0.8, muted_alpha=0.2, legend_label=name)

p.legend.location = "top_left"
p.legend.click_policy = "mute"

show(p)
