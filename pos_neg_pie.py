"""
Plotfile for the positive/negative pie chart
"""

import plotly
import plotly.graph_objs as go
import numpy as np

def pos_neg_pie(emotions):
	data =  [{'labels': ['Positive', 'Negative'],
	              'values': [emotions['positive'], emotions['negative']],
	              'type': 'pie'}]

	layout = go.Layout(
    autosize=False,
    width=300,
    height=300,
    title='Positive Negative'
	)
	fig = go.Figure(data=data, layout=layout)

	plotly.offline.plot(fig, filename='static/graphs/pos_neg_pie.html')