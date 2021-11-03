import matplotlib.pyplot as plt
import numpy as np


x = np.arange(10)
y = 2.5 * np.sin(x / 20 * np.pi)
yerr = np.linspace(0.05, 0.2, 10)


fig = plt.figure(figsize=(10, 10))
plt.errorbar(x, y + 3, yerr=yerr, label="both limits (default)")
plt.errorbar(x, y + 2, yerr=yerr, label="uplims=True", uplims=True)
plt.errorbar(x, y + 1, yerr=yerr, label="uplims=True, lolims=True", 
             uplims=True, lolims=True)
upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits,
            label="subsets of uplims & lolims")
plt.legend(loc="lower right")
plt.show()




x = np.arange(10) / 10
y0 = (x + 0.1)**2
y1 = (x + 0.1)**3
y2 = (x + 0.1)**4



fig = plt.figure(figsize=(10,10))
plt.errorbar(x, y0, xerr=0.1, xlolims=True, label="xlolims=True")
plt.errorbar(x+0.6, y1, xerr=0.1, xlolims=lowerlimits, xuplims=upperlimits, label="subsets of xuplims and xlolims")
plt.errorbar(x+1.2, y2, xerr=0.1, xuplims=True, label="xuplims=True")
plt.legend(loc="upper left")
plt.show()



