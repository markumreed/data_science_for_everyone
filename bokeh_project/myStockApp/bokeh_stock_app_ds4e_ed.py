import pandas as pd
from functools import lru_cache
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, PreText, Select
from bokeh.plotting import figure

DEFAULT_TICKERS = ["AAPL", "MSFT", "FB", "IBM", "GOOG"]


@lru_cache()
def load_ticker(ticker):
    data = pd.DataFrame(ticker, parse_dates=['date'])
    data.set_index("date", inplace=True)
    data[ticker+'_returns'] = data.diff()
    return data

