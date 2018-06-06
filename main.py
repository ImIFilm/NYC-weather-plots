import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation


from dataParser import DataParser
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')


x = DataParser('weatherNYC.csv')
plt.plot(x.dates, x.avgs)
plt.title('temperatura w NYC w 2016 (w ℉)')
plt.show()