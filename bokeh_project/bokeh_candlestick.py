import pandas as pd
import yfinance as yf
from math import pi

from bokeh.plotting import figure, show

data = yf.download('pfe', start='2021-01-01', end ='2021-07-01' )
data.reset_index(inplace=True)

inc = data['Close'] > data['Open']
dec = data['Open'] > data['Close']

w = 12*60*60*1000 # trading time in ms

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

p = figure(x_axis_type="datetime", plot_width=1000, tools=TOOLS, title = "Pfizer Candlestick Chart")
p.xaxis.major_label_orientation = pi/4
p.grid.grid_line_alpha = 0.3

p.segment(data['Date'], data['High'], data['Date'], data['Low'], color='black')
p.vbar(data['Date'][inc], w, data['Open'][inc], data['Close'][inc], fill_color="blue", line_color="black")
p.vbar(data['Date'][dec], w, data['Open'][dec], data['Close'][dec], fill_color="red", line_color="black")
show(p)


