from processByMonths import ProcessByMonths
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import style

class VisualizationByMonths:
    def __init__(self, obj):
        self.obj=obj
        self.months_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    @property
    def min_temp_list(self):
        min=[]
        for i in range (len(self.months_list)):
            x = ProcessByMonths(i+1)
            min.append(x.mmin)
        return min

    @property
    def max_temp_list(self):
        max=[]
        for i in range (len(self.months_list)):
            x = ProcessByMonths(i+1)
            max.append(x.mmax)
        return max

    @property
    def avg_temp_list(self):
        avg = []
        for i in range(len(self.months_list)):
            x = ProcessByMonths(i + 1)
            avg.append(x.mavg)
        return avg

    def show_plot(self):
        blue_patch = mpatches.Patch(color='blue', label='temperatura minimalna')
        plt.plot(self.months_list, self.min_temp_list, '.b-')
        red_patch = mpatches.Patch(color='red', label='temperatura maksymalna')
        plt.plot(self.months_list, self.max_temp_list, '.r-')
        green_patch = mpatches.Patch(color='green', label='temperatura średnia')
        plt.plot(self.months_list, self.avg_temp_list, 'og--')
        plt.legend(handles=[red_patch, blue_patch, green_patch])
        plt.title("Temperatura w NYC z podzialem na miesiace 2016 (w ℉)")
        plt.show()

#x=VisualizationByMonths(3)
x.show_plot()
#print(x.min_temp_list)