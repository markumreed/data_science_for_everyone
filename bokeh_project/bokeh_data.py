from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
import seaborn as sns

data = sns.load_dataset("tips") # pandas DataFrame

# create ColumnDataSource based dictionary
source = ColumnDataSource(data=data)

# Create figure
p = figure()

# Make scatterplot
p.circle(x="total_bill", y="tip", size=10, source=source)

show(p)