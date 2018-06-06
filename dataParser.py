import csv
from datetime import datetime

#zczytuje dane z csv
class DataParser:
    def __init__(self, file):
        self.file=file

    @property
    def dates(self):
        dates=[]
        with open(self.file, 'r') as csvfile:
            tt = csv.reader(csvfile, delimiter=',')
            for row in tt:
                dates.append(datetime.strptime(row[0], '%d-%m-%Y'))
        return dates

    @property
    def maxs(self):
        maxs = []
        with open(self.file, 'r') as csvfile:
            tt = csv.reader(csvfile, delimiter=',')
            for row in tt:
                maxs.append(float(row[1]))
        return maxs

    @property
    def mins(self):
        mins = []
        with open(self.file, 'r') as csvfile:
            tt = csv.reader(csvfile, delimiter=',')
            for row in tt:
                mins.append(float(row[2]))
        return mins

    @property
    def avgs(self):
        avgs = []
        with open(self.file, 'r') as csvfile:
            tt = csv.reader(csvfile, delimiter=',')
            for row in tt:
                avgs.append(float(row[3]))
        return avgs

    @property
    def precipations(self):
        precipations = []
        with open(self.file, 'r') as csvfile:
            tt = csv.reader(csvfile, delimiter=',')
            for row in tt:
                precipations.append(float(row[4]))
        return precipations