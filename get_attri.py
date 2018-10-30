import pandas as pd
from datetime import datetime

class get_attri:
    def __init__(self):
        #t_runs,n_out,bf,four,six,bf_b,inn,run_b,over,bb,wick,w4,w5=self.get_detail(name,date)
        pass
        #hardhit,finisher,fastscorer,consistent,running,economy,wicket_taker,consistent_ball,big_wicket_taker,shortperformance=self.get_ten(t_runs,n_out,bf,four,six,bf_b,inn,run_b,over,bb,wick,w4,w5)
    def get_detail(self,name,date):
        t_runs,n_out,bf,four,six,bf_b,inn,matches,run_b,over,bb,wick,w4,w5=0,0,0,0,0,0,0,0,0,0,0,0,0,0
        players=[]
        match=1
        df = pd.read_pickle('data/8-18')
        for i, r in df.iterrows():
            if r['date']>=date:
                break
            if r['name']==name:
                if r['m_id'] != match:
                    match=r['m_id']
                    players=[]
                t_runs=t_runs+r['run']
                if int(r['isout'])==1:
                    n_out=n_out+1
                bf = bf + r['ball']
                four = four +r['4s']
                six= six + r['6s']
                run_b=r['r_b'] + run_b
                wick= wick + r['wicket']
                if r['wicket']==4:
                    w4=w4+1
                elif r['wicket']>=5:
                    w5=w5+1
                over = over +int(r['over'])
                bb=bb +int(r['over'])*6 + (r['over']-int(r['over']))*10
                if r['name'] not in players:
                    matches=matches+1
                    players.insert(0,r['name'])
        inn= matches
        bf_b=bf-(four+six)



        return t_runs,n_out,bf,four,six,bf_b,inn,run_b,over,bb,wick,w4,w5

    def get_ten(self,t_runs,n_out,bf,four,six,bf_b,inn,run_b,over,bb,wick,w4,w5):
        try:
            hardhit=(4*four +6*six)/bf
        except:
            hardhit=0
        try:
            finisher=n_out/inn
        except:
            finisher=0
        try:
            fastscorer=t_runs/bf
        except:
            fastscorer=0
        try:
            consistent=t_runs/n_out
        except:
            consistent=0
        try:
            running= (t_runs-(4*four +6*six))/bf_b
        except:
            running=0
        try:
            economy=run_b/over
        except:
            economy=0
        try:
            wicket_taker=bb/wick
        except:
            wicket_taker=0
        try:
            consistent_ball=run_b/wick
        except:
            consistent_ball=0
        try:
            big_wicket_taker=(w4+w5)/inn
        except:
            big_wicket_taker=0
        try:
            shortperformance=(wick-4*w4-5*w5)/(inn-w4-w5)
        except:
            shortperformance=0
        return hardhit,finisher,fastscorer,consistent,running,economy,wicket_taker,consistent_ball,big_wicket_taker,shortperformance
    def get_bb(self,name,date):
        date= datetime.strptime(date,"%Y-%m-%d")
        t_runs,n_out,bf,four,six,bf_b,inn,run_b,over,bb,wick,w4,w5=self.get_detail(name,date)
        hardhit,finisher,fastscorer,consistent,running,economy,wicket_taker,consistent_ball,big_wicket_taker,shortperformance=self.get_ten(t_runs,n_out,bf,four,six,bf_b,inn,run_b,over,bb,wick,w4,w5)
        bat=consistent*0.485+fastscorer*0.0275
        ball=consistent_ball*0.3011+shortperformance*0.3001+wicket_taker*0.1429
        return bat,ball
    def get_toss(self,x,y):
        if x==y:
            return 1
        else:
            return 0
    def get_inn(self,x):
        if x=='bat':
            return 1
        else:
            return 0
    def get_captain(self,x):
        q=x.find('(c')
        if q==-1:
            return 0
        else:
            return 1
    def clear_player(self,x):
        x = (x.replace(' (c)','')).replace(' (wk)','').replace(' (c & wk)','')
        return x

# bat,ball=x.get_bb(name,date)
# print(bat)
# print(ball)
