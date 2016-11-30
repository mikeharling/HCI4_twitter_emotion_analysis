"""
Plot file for the polar radar scatter chart
"""

import plotly
import plotly.graph_objs as go
import numpy as np

def plotPolarScatterChart(emotions, search_query, total_tweets):
    start = 1
    title = "Search Term: " + search_query
    divide = 1

    if total_tweets > 125:
        divide = 3

    trace1 = go.Scatter(
        r=np.random.uniform(start,emotions['joy'],size=emotions['joy']/divide),
        t=np.random.uniform(5,40,size=emotions['joy']),
        mode='markers',
        name='Joy',
        marker=dict(
            color='rgb(102,166,30)',
            size=110,
            line=dict(
                color='white'
            ),
            opacity=0.7
        )
    )
    trace2 = go.Scatter(
        r=np.random.uniform(start,emotions['surprise'],size=emotions['surprise']/divide),
        t=np.random.uniform(50,85,size=emotions['surprise']),
        mode='markers',
        name='Surprise',
        marker=dict(
            color='rgb(27,158,119)',
            size=110,
            line=dict(
                color='white'
            ),
            opacity=0.7
        )
    )
    trace3 = go.Scatter(
        r=np.random.uniform(start,emotions['anticipation'],size=emotions['anticipation']/divide),
        t=np.random.uniform(95,130,size=emotions['anticipation']),
        mode='markers',
        name='Anticipation',
        marker=dict(
            color='rgb(231,41,138)',
            size=110,
            line=dict(
                color='white'
            ),
            opacity=0.7
        )
    )
    trace4 = go.Scatter(
        r=np.random.uniform(start,emotions['trust'],size=emotions['trust']/divide),
        t=np.random.uniform(140,175,size=emotions['trust']),
        mode='markers',
        name='Trust',
        marker=dict(
            color='rgb(117,112,179)',
            size=110,
            line=dict(
                color='white'
            ),
            opacity=0.7
        )
    )
    trace5 = go.Scatter(
        r=np.random.uniform(start,emotions['sadness'],size=emotions['sadness']/divide),
        t=np.random.uniform(185,220,size=emotions['sadness']),
        mode='markers',
        name='Sadness',
        marker=dict(
            color='rgb(230,171,2)',
            size=110,
            line=dict(
                color='white'
            ),
            opacity=0.7
        )
    )
    trace6 = go.Scatter(
        r=np.random.uniform(start,emotions['fear'],size=emotions['fear']/divide),
        t=np.random.uniform(230,265,size=emotions['fear']),
        mode='markers',
        name='Fear',
        marker=dict(
            color='rgb(81,81,81)',
            size=110,
            line=dict(
                color='white'
            ),
            opacity=0.7
        )
    )
    trace7 = go.Scatter(
        r=np.random.uniform(start,emotions['anger'],size=emotions['anger']/divide),
        t=np.random.uniform(275,310,size=emotions['anger']),
        mode='markers',
        name='Anger',
        marker=dict(
            color='rgb(176,23,1)',
            size=110,
            line=dict(
                color='white'
            ),
            opacity=0.7
        )
    )
    trace8 = go.Scatter(
        r = np.random.uniform(start,emotions['disgust'],size=emotions['disgust']/divide),
        t = np.random.uniform(320,355,size=emotions['disgust']),
        mode='markers',
        name='Disgust',
        marker=dict(
            color='rgb(217,95,2)',
            size=110,
            line=dict(
                color='white'
            ),
            opacity=0.7
        )
    )
    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8]
    layout = go.Layout(
        title=title,
        xaxis=dict(
            showticklabels='FALSE',
            showgrid='FALSE',
            showtickprefix='none',
            rangeselector=dict(
                visible='FALSE')),
        font=dict(
            size=15
        ),
        plot_bgcolor='rgb(223, 223, 223)',
        angularaxis=dict(
            tickcolor='rgb(253,253,253)'
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='static/graphs/polarScatterChart.html')