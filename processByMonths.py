from dataParser import DataParser


# Przetwarzanie danych na potrzeby wizualizacji roku z przedzialka miesieczna
class ProcessByMonths:
    def __init__(self, month):
        self.month = month

    @property
    def mmax(self):
        mmax = -500

        x = DataParser('weatherNYC.csv')
        dates = x.dates
        maxs = x.maxs
        for i in range(len(dates)):
            if (dates[i].month == self.month):
                if (maxs[i] > mmax):
                    mmax = maxs[i]
        return mmax

    @property
    def mmin(self):
        mmin = 1000

        x = DataParser('weatherNYC.csv')
        dates = x.dates
        mins = x.mins
        for i in range(len(dates)):
            if (dates[i].month == self.month):
                if (mins[i] < mmin):
                    mmin = mins[i]
        return mmin

    @property
    def mavg(self):
        sum = 0
        counter = 0
        x = DataParser('weatherNYC.csv')
        for i in range(len(x.dates)):
            if (x.dates[i].month == self.month):
                sum = sum + x.avgs[i]
                counter = counter + 1
        return sum / counter

d=ProcessByMonths(2)
d.mavg
