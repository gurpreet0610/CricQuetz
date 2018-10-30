import plotly.graph_objs as go
import plotly.tools as tls
tls.set_credentials_file(username='gurpreets0610', api_key='DNaueCR9iJx1M8694SOh')
import plotly.offline as py

class plotly_charts:

    def teams_gram(self,seasons,team1,team2,final1,final2):
        trace1 = go.Bar(
            x=seasons,
            y=final1,
            name=team1  
        )
        trace2 = go.Bar(
            x=seasons,
            y=final2,
            name=team2
        )

        data = [trace1, trace2]
        layout = go.Layout(
            title= 'Teams Comparision',
            barmode='group',
            hovermode= 'closest',
            xaxis=dict(
                showgrid=False,
                zeroline=False,
                showline=False,
                title='Seasons'
            ),
            yaxis=dict(
                title= 'Wins',
                ticklen= 5,
                gridwidth= 2,
                showgrid=False,
                zeroline=False,
                showline=False
            ),
            showlegend= False
            )

        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig,output_type="div")

    def bats_gram(self,play):
        players=[]
        score=[]
        for i in play:
            players.append(i[0])
            score.append(i[1])
        data = [go.Bar(
            x=players,
            y=score
            )   ]
        layout = go.Layout(
            title= 'Top 10 Scoring Batsman',
            hovermode= 'closest',
            xaxis=dict(
                showgrid=False,
                zeroline=False,
                showline=False,
                title='Batsman'
            ),
            yaxis=dict(
                title= 'Total Runs',
                ticklen= 5,
                gridwidth= 2,
                showgrid=False,
                zeroline=False,
                showline=False
            ),
            showlegend= False
            )

        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig,output_type="div")


    def get_bowl_list(self,play):
        players=[]
        wickets=[]
        economy=[]
        for i in play:
            players.append(i[0])
            wickets.append(i[1])
            economy.append(i[2])
        return players,wickets,economy

    def bowl_chart(self,play):
        bowlers,wickets,economy= self.get_bowl_list(play)
        trace = go.Scatter(
        y = wickets,
        x = bowlers,
        mode='markers',
        marker=dict(
            size= wickets,
            color = economy,
            colorscale='Viridis',
            showscale=True,
            colorbar = dict(title = 'Economy'),
          ),
        )
        data = [(trace)]

        layout= go.Layout(
        autosize= True,
        title= 'Top 10 Wicket Taking Bowlers',
        hovermode= 'closest',
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            title='Bowlers'
        ),
        yaxis=dict(
            title= 'Wickets Taken',
            ticklen= 5,
            gridwidth= 2,
            showgrid=False,
            zeroline=False,
            showline=False
        ),
        showlegend= False
        )
        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig,output_type="div")