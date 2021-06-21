import pandas as pd
from bokeh.plotting import show
from bokeh.models import ColumnDataSource, DataTable, TableColumn
from bokeh.sampledata.stocks import AAPL

df = pd.DataFrame(AAPL)
stats = df.describe().reset_index()

source = ColumnDataSource(stats)
#columns = [TableColumn(field=col, title=col) for col in stats.columns]

columns = [
    TableColumn(field="index", title="Stat"),
    TableColumn(field="open", title="Open"),
    TableColumn(field="high", title="High"),
    TableColumn(field="low", title="Low"),
    TableColumn(field="close", title="Close"),
    TableColumn(field="volume", title="Volume"),
    TableColumn(field="adj_close", title="Adjusted Close")
]

data_table = DataTable(source=source, columns=columns, 
width=800, height=400, index_position=None)

show(data_table)