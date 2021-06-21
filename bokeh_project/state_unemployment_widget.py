from bokeh.models.annotations import Title
from bokeh.plotting import figure, show
from bokeh.models import LogColorMapper, ColumnarDataSource
from bokeh.palettes import Viridis6 as palette
from bokeh.sampledata.unemployment import data as unemployment # dictionary
from bokeh.sampledata.us_counties import data as counties # dictionary
from bokeh.models import Select
from bokeh.layouts import row




palette = tuple(reversed(palette))
color_mapper = LogColorMapper(palette=palette)

# Select
data = dict()
state_codes = list(set([county['state'] for code, county in counties.items()]))
select = Select(title="Please Select a State:", value="ar", options=state_codes)
def call_back(attr, old, new):
    global counties
    global data
    counties = {
        code: county for code, county in counties.items() if county['state'] == select.value
    }

    county_xs = [county['lons'] for county in counties.values()]
    county_ys = [county['lats'] for county in counties.values()]

    county_names = [county['name'] for county in counties.values()]
    county_rates = [unemployment[county_id] for county_id in counties]

    data = dict(
        x=county_xs,
        y=county_ys,
        name=county_names,
        rate=county_rates
    )
select.on_change('value', call_back)



TOOLS = "pan,wheel_zoom,reset,hover,save"

p = figure(
    title="Unemployment, 2009",tools=TOOLS,
    x_axis_location=None, y_axis_location=None,
    tooltips=[
        ("Name", "@name"), ("Unemployment Rate", "@rate"), ("(Long, Lat)", "($x, $y)")
    ]
)

p.grid.grid_line_color=None
p.hover.point_policy = "follow_mouse"


p.patches("x", "y", source=data, fill_color={"field": "rate", "transform":color_mapper},
fill_alpha=0.6, line_color="black", line_width=0.5)

show(row([select, p]))
