from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.sampledata.sprint import sprint as df

df['Year'] = df['Year'].astype(str)
group = df.groupby("Year")
source = ColumnDataSource(group)

p = figure(y_range=group, x_range=(9.5, 12.8), plot_width=500, plot_height=500, 
toolbar_location=None, tools="", title="Time Spread for Sprint Medalists (by year)")
p.hbar(y="Year", left="Time_min", right="Time_max", height=0.4, source=source)
p.outline_line_color = None
p.ygrid.grid_line_color=None
p.xaxis.axis_label = "Time in seconds"

show(p)