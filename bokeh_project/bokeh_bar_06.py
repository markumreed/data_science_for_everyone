from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral5
from bokeh.sampledata.autompg import autompg_clean as df
from bokeh.transform import factor_cmap

df['cyl'] = df['cyl'].astype(str)
print(df.head())
group = df.groupby(['cyl', 'mfr'])
source = ColumnDataSource(data=group)

cyl_mfr_cmap = factor_cmap("cyl_mfr", palette=Spectral5, factors = sorted(df['cyl'].unique()), end=1)


p = figure(plot_width=800, plot_height=400, title = "Mean MPG by # Cylinders and Manufacturers",
x_range=group, toolbar_location=None, tooltips=[("MPG", "@mpg_mean"), ("Cyl, Mfr", "@cyl_mfr")])

p.vbar(x="cyl_mfr", top="mpg_mean", width=1, source=source, line_color="white", fill_color=cyl_mfr_cmap)

p.y_range.start = 0
p.x_range.range_padding = 0.05
p.xgrid.grid_line_color = None
p.xaxis.major_label_orientation = 1.2
p.outline_line_color = None


show(p)



# p = figure(plot_height= 400, x_range=group, title="MPG by # Cylinders", 
# toolbar_location=None, tools="")

# p.vbar(x="cyl", top="mpg_mean", width=1, source=source,
# line_color=cyl_cmap, fill_color=cyl_cmap)
# p.y_range.start = 0
# p.xgrid.grid_line_color = None
# show(p)