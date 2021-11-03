import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.factorplots import interaction_plot
get_ipython().run_line_magic("matplotlib", " inline")


np.random.seed(42)
weight = pd.Series(np.repeat(['low','high', 'low', 'high'], 15), name="weight")
intake = pd.Series(np.repeat(['low_carb','hi_carb'], 30), name="intake")
days = np.log(np.random.randint(1, 30, size=60))


fig, ax = plt.subplots(figsize=(10, 10))
fig = interaction_plot(
    x=weight,
    trace=intake,
    response=days,
    colors=['firebrick', 'navy'],
    markers=['^','D'],
    ms=10,
    ax=ax
)



