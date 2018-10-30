import csv

class players:
    def __init__(self):
        pass
    def get_players(self,team):
        with open('data/squad.csv', mode='r') as fl:
            csv_reader = csv.reader(fl,delimiter=',')
            for row in csv_reader:
                try:
                    if row[0]==team:
                        return row[1:]
                except:
                    pass

        return 0
