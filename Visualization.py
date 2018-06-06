from dataParser import DataParser
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')


x = DataParser('weatherNYC.csv')
plt.plot(x.dates, x.maxs)
plt.plot(x.dates, x.mins)





plt.title('Interesting Graph\nCheck it out')
plt.show()

