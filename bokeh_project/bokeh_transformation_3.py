from bokeh.plotting import figure, show
from bokeh.transform import linear_cmap
import numpy as np

N=4000
data = dict(x=np.random.random(size=N)*100,
y = np.random.random(size=N) * 100,
r = np.random.random(size=N) * 1.5

)
p = figure()
p.circle("x", "y", radius="r", source=data, fill_alpha=0.5,
color=linear_cmap("x", "Viridis256", 0, 100))
show(p)