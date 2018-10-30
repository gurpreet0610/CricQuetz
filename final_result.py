import csv
import pickle
import numpy as np
from charts import chart
"""
0. toss  --> (Home team=== Toss Win)?1:0
1. inning --> (bat)?1:0 $ When toss winning team choose bat:1
(2,3,4=captian,bat,ball)*22 --->66 + 2 = 68
"""
class finale:

    def __init__(self):
        pass
    def result(self,info):
        toss,inning,t1,t2,p1,p2,c1,c2=self.parse_json(info)
        data=self.prep_row(toss,inning,t1,t2,p1,p2,c1,c2)
        data=self.str_float(data)
        data=np.array(data)
        data=data.reshape(1,-1)
        path='models/test_model.pkl'
        model=self.load_model(path)
        x=model.predict(data)
        if x[0] == 1:
            return t1
        else:
            return t2

    def parse_json(self,info):
        toss=info['team'][2]['toss']
        inning=info['team'][3]['inning']
        t1=info['team'][0]['name']
        t2=info['team'][1]['name']
        p1=info['team'][0]['member']
        p2=info['team'][1]['member']
        c1=info['team'][0]['captainName']
        c2=info['team'][1]['captainName']
        return toss,inning,t1,t2,p1,p2,c1,c2

    def prep_row(self,toss,inning,t1,t2,p1,p2,c1,c2):
        r=[]
        r.append(self.get_toss(toss,t1))
        r.append(self.get_inn(inning))
        r= r+self.prep_players(p1,c1)
        r= r+self.prep_players(p2,c2)
        return r

    def get_bb(self,name):
        with open('data/players_main.csv', mode='r') as fl:
            csv_reader = csv.reader(fl,delimiter=',')
            for row in csv_reader:
                try:
                    if row[0]==name:
                        return row[1],row[2]
                except:
                        return 0,0

    def get_toss(self,x,y):
        if x==y:
            return 1
        else:
            return 0

    def get_inn(self,inn):
        if inn == 'bat':
            return 1
        else:
            return 0

    def prep_players(self,p,c):
        r=[]
        for pl in p:
            cap=0
            if c==p:
                cap=1
            bat,ball=self.get_bb(pl)
            r.append(cap)
            r.append(bat)
            r.append(ball)
        
        return r

    def load_model(self,path):
        with open(path, 'rb') as pickle_file:
            content = pickle.load(pickle_file)

        return content

    def str_float(self,data):
        r=[]
        for i in data:
            r.append(float(i))
        return r


    def finale_result(self,info):
        c=chart()
        toss,inning,t1,t2,p1,p2,c1,c2=self.parse_json(info)
        res=self.result(info)
        print(t1)
        print(t2)
        teams_chart=c.team1_vs_team2(t1,t2)
        players=p1+p2
        bats_chart=c.batsman_10(players)
        bowls_chart=c.bowler_10(players)
        z={"winner":res,
        "teams_chart":teams_chart,
        'bats_chart':bats_chart,
        'bowls_chart':bowls_chart
        }
        return z


x=finale()
data={
    "team": [
       {
          "name": "Kings XI Punjab",
          "member": [
             "Mayank Agarwal",
             "Axar Patel",
             "Yuvraj Singh",
             "Karun Nair",
             "Lokesh Rahul",
             "Mujeeb Ur Rahman",
             "David Miller",
             "Aaron Finch",
             "Marcus Stoinis",
             "Ravichandran Ashwin",
             "Ankit Rajpoot"
          ],
          "captainName": "Mujeeb Ur Rahman"
       },
       {
          "name": "Delhi Daredevils",
          "member": [
             "Shreyas Iyer",
             "Rishabh Pant",
             "Glenn Maxwell",
             "Gautam Gambhir",
             "Jason Roy",
             "Colin Munro",
             "Mohammed Shami",
             "Amit Mishra",
             "Prithvi Shaw",
             "Rahul Tewatia",
             "Vijay Shankar"
          ],
          "captainName": "Gautam Gambhir"
       },
       {"toss":"Kings XI Punjab"},
       {"inning":"bat"}
    ]
 }
# print(x.finale_result(data))





