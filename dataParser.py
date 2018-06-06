import csv
from datetime import datetime

#zczytuje dane z csv
class DataParser:
    def __init__(self, file):
        self.file=file

    @property
    def dates(self):
        dates=[]
        try:
            with open(self.file, 'r') as csvfile:
                tt = csv.reader(csvfile, delimiter=',')
                for row in tt:
                    dates.append(datetime.strptime(row[0], '%d-%m-%Y'))
        except FileNotFoundError:
            print("problemy z nazwami pliku csv")
            exit(-1)
        return dates

    @property
    def maxs(self):
        maxs = []
        try:
            with open(self.file, 'r') as csvfile:
                tt = csv.reader(csvfile, delimiter=',')
                for row in tt:
                    maxs.append(float(row[1]))
        except FileNotFoundError:
            print("problemy z nazwami pliku csv")
            exit(-1)
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
        try:
            with open(self.file, 'r') as csvfile:
                tt = csv.reader(csvfile, delimiter=',')
                for row in tt:
                    avgs.append(float(row[3]))
        except FileNotFoundError:
            print("problemy z nazwami pliku csv")
            exit(-1)
        return avgs

    @property
    def precipations(self):
        pres = []
        try:
            with open(self.file, 'r') as csvfile:
                tt = csv.reader(csvfile, delimiter=',')
                for row in tt:
                    if (not row[4].isalpha()):
                        pres.append(float(row[4]))
                    else:
                        pres.append(0)
        except FileNotFoundError:
            print("problemy z nazwami pliku csv")
            exit(-1)
        return pres
