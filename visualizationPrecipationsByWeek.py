from processPrecipationsByWeek import ProcessPrecipationsByWeek
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import style

class VisualizationPrecipationsByWeeks:
    def __init__(self, obj):
        self.obj=obj
        self.week_list=[]
        for s in range (1, 52):
            self.week_list.append(s)

    @property
    def pres_temp_list(self):
        pres = []
        for i in range(len(self.week_list)):
            x = ProcessPrecipationsByWeek(i + 1)
            pres.append(x.wpre)
        return pres

    def show_plot(self):
        blue_patch = mpatches.Patch(color='blue', label='opady')
        plt.plot(self.week_list, self.pres_temp_list, '.b-')
        plt.legend(handles=[blue_patch])
        plt.title("Opady w NYC z podzialem na tygodnie 2016 w mm")
        plt.show()

x=VisualizationPrecipationsByWeeks(3)
print (x.pres_temp_list)
x.show_plot()
#print(x.min_temp_list)