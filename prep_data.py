import csv
from get_attri import get_attri

class prep_data:

    def __init__(self):
        players=[]
        players=self.get_play()
        self.generate_csv(players)

    def get_play(self):
        players=[]
        with open('data/squad.csv', mode='r') as fl:
            csv_reader = csv.reader(fl,delimiter=',')
            for row in csv_reader:
                try:
                    if len(row[0])!=None:
                        players=players +row[1:]
                except:
                    pass

        return players


    def generate_csv(self,players):
        g= get_attri()
        date='2018-10-6'
        for p in players:
            try:
                bat,ball=g.get_bb(p,date)
            except:
                bat,ball=0,0
            l=[p,bat,ball]
            with open('data/players_main.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(l)


                
x= prep_data()