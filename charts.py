import pandas as pd
import csv
from plotly_graph import plotly_charts as pc

class chart:
    def team1_vs_team2(self,team1,team2):
        test = self.get_win_csv(team1,team2)
        x=test[0].unique()
        y=[]
        final1=[]
        final2=[]
        for i in x:
            y.append(str(i))
            t1=0.00
            t2=0.00
            for index,r in test.iterrows():
                if r[0]==i:
                    if r[1]==team1:
                        t1=r[2]
                    if r[1]==team2:
                        t2=r[2]
            final1.append(str(t1))
            final2.append(str(t2))
        q=pc()
        z=q.teams_gram(y,team1,team2,final1,final2)
        return z          

    def get_win_csv(self,team1,team2):
        df=pd.read_csv("final_data/win.csv")
        mt1=df[((df['team1']==team1)|(df['team2']==team1))&((df['team1']==team2)|(df['team2']==team2))]
        x=mt1.groupby(['season','winner'])['winner'].count()
        x.to_csv("final_data/test.csv")
        df=pd.read_csv("final_data/test.csv",header=None)
        return df

    def takeSecond(self,elem):
        return elem[1]

    def batsman_10(self,players):
        play=[]
        df=pd.read_csv("final_data/total_run.csv",header=None)
        for i,r in df.iterrows():
            if r[0] in players:
                j=( r[0],r[1])   
                play.append(j)
        x=pc()
        play.sort(key=self.takeSecond,reverse=True)
        chart=x.bats_gram(play[:10])
        return chart

    def bowler_10(self,players):
        play=[]
        df=pd.read_csv("final_data/total_economy.csv",header=None)
        for i,r in df.iterrows():
            if r[0] in players:
                j=( r[0],int(r[2]),r[1])   
                play.append(j)
        x=pc()
        play.sort(key=self.takeSecond,reverse=True)
        return x.bowl_chart(play[:10])



