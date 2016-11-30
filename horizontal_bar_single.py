"""
Plot file for the horizontal bar chart
"""

import plotly
import plotly.graph_objs as go

def horiz_bar_single(emotions, search_term):
    positive = emotions['joy'] + emotions['surprise'] + emotions['anticipation'] + emotions['trust']
    negative = emotions['fear'] + emotions['sadness'] + emotions['anger'] + emotions['disgust']

    trace1 = go.Bar(
        y=[search_term],
        x=[emotions['joy']],
        name='Joy',
        orientation = 'h',
        marker = dict(
            color = 'rgb(102,166,30)',
            line = dict(
                color = 'rgba(58, 71, 80, 1.0)',
                width = 3)
        )
    )
    trace2 = go.Bar(
        y=[search_term],
        x=[emotions['surprise']],
        name='Surprise',
        orientation = 'h',
        marker = dict(
            color = 'rgb(27,158,119)',
            line = dict(
                color = 'rgba(58, 71, 80, 1.0)',
                width = 3)
        )
    )
    trace3 = go.Bar(
        y=[search_term],
        x=[emotions['anticipation']],
        name='Anticipation',
        orientation = 'h',
        marker = dict(
            color = 'rgb(231,41,138)',
            line = dict(
                color = 'rgba(58, 71, 80, 1.0)',
                width = 3)
        )
    )
    trace4 = go.Bar(
        y=[search_term],
        x=[emotions['trust']],
        name='Trust',
        orientation = 'h',
        marker = dict(
            color = 'rgb(117,112,179)',
            line = dict(
                color = 'rgba(58, 71, 80, 1.0)',
                width = 3)
        )
    )
    trace5 = go.Bar(
        y=[search_term],
        x=[emotions['sadness']],
        name='Sadness',
        orientation = 'h',
        marker = dict(
            color = 'rgb(230,171,2)',
            line = dict(
                color = 'rgba(58, 71, 80, 1.0)',
                width = 3)
        )
    )
    trace6 = go.Bar(
        y=[search_term],
        x=[emotions['fear']],
        name='Fear',
        orientation = 'h',
        marker = dict(
            color = 'rgb(81,81,81)',
            line = dict(
                color = 'rgba(58, 71, 80, 1.0)',
                width = 3)
        )
    )
    trace7 = go.Bar(
        y=[search_term],
        x=[emotions['anger']],
        name='Anger',
        orientation = 'h',
        marker = dict(
            color = 'rgb(176,23,1)',
            line = dict(
                color = 'rgba(58, 71, 80, 1.0)',
                width = 3)
        )
    )
    trace8 = go.Bar(
        y=[search_term],
        x=[emotions['disgust']],
        name='Disgust',
        orientation = 'h',
        marker = dict(
            color = 'rgb(217,95,2)',
            line = dict(
                color = 'rgba(58, 71, 80, 1.0)',
                width = 3)
        )
    )
    trace9 = go.Bar(
        y=['Pos/Neg'],
        x=[positive],
        name='Positive',
        orientation = 'h',
        marker = dict(
            color = 'rgb(203,0,0)',
            line = dict(
                color = 'rgba(58, 71, 80, 1.0)',
                width = 3)
        )
    )
    trace10 = go.Bar(
        y=['Pos/Neg'],
        x=[negative],
        name='Negative',
        orientation = 'h',
        marker = dict(
            color = 'rgb(0,0,142)',
            line = dict(
                color = 'rgba(58, 71, 80, 1.0)',
                width = 3)
        )
    )


    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10]
    layout = go.Layout(
        barmode='stack'
    )

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='templates/horizontal-bar-single.html')