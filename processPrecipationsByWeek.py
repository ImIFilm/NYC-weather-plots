from dataParser import DataParser

#Przetwarzanie danych na potrzeby wizualizacji opadkow z tygodnia na tydzien
class ProcessPrecipationsByWeek:
    def __init__(self, week: object) -> object:
        self.week = week

    @property
    def wpre(self):
        x = DataParser('weatherNYC.csv')
        sum=0
        for i in range(360):
            if(x.dates[i].isocalendar()[1]==self.week):
                sum=sum+x.precipations[i]
        return sum


#for i in range (10):
    #x=ProcessPrecipationsByWeek(i)
    #print (x.wpre)
