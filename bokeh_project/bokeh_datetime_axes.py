import random
from datetime import datetime, timedelta

from bokeh.models import DatetimeTickFormatter, NumeralTickFormatter
from bokeh.plotting import figure, show

# generate list of dates 25 days
dates = [(datetime.now() + timedelta(day * 7)) for day in range(0, 26)]

# generate 25 random data points

y = random.sample(range(0,100), 26)

# create figure
p = figure(
    title="Datetime Axis Example",
    x_axis_type="datetime",
    sizing_mode="stretch_width",
    max_width=900,
    plot_height = 300,
)

# Renderers
p.circle(dates, y, size=5)
p.line(dates, y, color="blue", line_width=2)

# formating
p.yaxis[0].formatter = NumeralTickFormatter(format="$0.00")
p.xaxis[0].formatter = DatetimeTickFormatter(months="%b %Y")

#show
show(p)