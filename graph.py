"""import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()"""
"""import matplotlib.pyplot as plt
import plotly.plotly as py
# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api
y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
N = len(y)
x = range(N)
width = 1/1.5
plt.bar(x, y, width, color="blue")
fig = plt.gcf()
plot_url = py.plot_mpl(fig, filename='mpl-basic-bar')
"""

"""import plotly.plotly as py
from plotly.graph_objs import *

data = Data([
    Scatter(
        x=[1, 2],
        y=[3, 4]
    )
])

plot_url = py.plot(data, filename='my plot')"""

import pylab as pl
import datetime

data = """0 14-11-2003
1 15-03-1999
12 04-12-2012
33 09-05-2007
44 16-08-1998
55 25-07-2001
76 31-12-2011
87 25-06-1993
118 16-02-1995
119 10-02-1981
145 03-05-2014"""

values = []
dates = []

for line in data.split("\n"):
    x, y = line.split()
    values.append(int(x))
    dates.append(datetime.datetime.strptime(y, "%d-%m-%Y").date())

fig = pl.figure()
ax = pl.subplot(111)
ax.bar(dates, values, width=100)
ax.xaxis_date()