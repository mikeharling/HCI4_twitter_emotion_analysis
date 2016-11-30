import math
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.models import Label

# The functions scale_x_coords and scale_y_coords take a list of x and y coordinates (respectively) that correspond to the points
# forming the outermost octagon on the scale. They then iterate over a fixed range using a constant increment to create an
# octagonal scale.
def scale_x_coords(outer_x_coords):

	scale_x_coords = [outer_x_coords]

	for i in np.arange(0.2, 1, 0.2):

		x_coords =[]

		for x_coord in outer_x_coords:
			x_coords.append(x_coord * i)

		scale_x_coords.append(x_coords)

	return scale_x_coords

def scale_y_coords(outer_y_coords):

	scale_y_coords = [outer_y_coords]

	for i in np.arange(0.2, 1, 0.2):

		y_coords =[]

		for y_coord in outer_y_coords:
			y_coords.append(y_coord * i)

		scale_y_coords.append(y_coords)

	return scale_y_coords

def emotion_visualiser(emotions, search_query):
	output_file("templates/patches.html")

	# The x_range and the y_range of the plot must be slightly larger than the range over which the scale extends (i.e. (-1, 1) in both
	# the x and y axis) as the labels for the points of the octagon will be clipped if they are left at default.
	p = figure(plot_width=700, plot_height=700, toolbar_location=None, x_range=(-1.5, 1.5), y_range=(-1.5, 1.5), title="Search Query: " + search_query)

	# Disable axis, grid lines, plot outline and toolbar.
	p.axis.visible = False
	p.xgrid.grid_line_color = None
	p.ygrid.grid_line_color = None
	p.outline_line_color = None
	p.toolbar.active_drag = None
	p.toolbar.active_scroll = None
	p.toolbar.active_tap = None

	# The x and y co-ordinates of the points forming the outermost octagon in the graph.
	outer_x_coords = [1, (math.sqrt(2) / 2), 0, -(math.sqrt(2) / 2), -1, -(math.sqrt(2) / 2), 0, (math.sqrt(2) / 2)]
	outer_y_coords = [0, (math.sqrt(2) / 2), 1, (math.sqrt(2) / 2), 0, -(math.sqrt(2) / 2), -1, -(math.sqrt(2) / 2)]

	# # Create the octagonal scale.
	p.patches(scale_x_coords(outer_x_coords), scale_y_coords(outer_y_coords), fill_alpha=0, line_color='black', line_width=1.5)

	# Remove the 'positive' and 'negative' keys from the dictionary.
	del emotions['positive']
	del emotions['negative']

	# Determine the percentage of tweets that relate to a certain emotion (must be cast to a float to avoid integer truncation).
	sum_emotion_count = float(sum(emotions.values()))
	if sum_emotion_count == 0:
		sum_emotion_count = 1
		
	surprise_percent = (emotions['surprise'] / sum_emotion_count) * 100
	sadness_percent = (emotions['sadness'] / sum_emotion_count) * 100
	joy_percent = (emotions['joy'] / sum_emotion_count) * 100
	disgust_percent = (emotions['disgust'] / sum_emotion_count) * 100
	trust_percent = (emotions['trust'] / sum_emotion_count) * 100
	anger_percent = (emotions['anger'] / sum_emotion_count) * 100
	anticipation_percent = (emotions['anticipation'] / sum_emotion_count) * 100
	fear_percent = (emotions['fear'] / sum_emotion_count) * 100

	# Add labels to each of the outermost points of the scale.
	p.add_layout(Label(x=outer_x_coords[0], y=outer_y_coords[0], x_units='data', text='Surprise (' + str(int(surprise_percent)) + '%)', text_font_style='bold', text_align='left', text_baseline='middle'))
	p.add_layout(Label(x=outer_x_coords[1], y=outer_y_coords[1], x_units='data', text='Sadness (' + str(int(sadness_percent)) + '%)', text_font_style='bold', text_align='left'))
	p.add_layout(Label(x=outer_x_coords[2], y=outer_y_coords[2], x_units='data', text='Joy (' + str(int(joy_percent)) + '%)', text_font_style='bold', text_align='center'))
	p.add_layout(Label(x=outer_x_coords[3], y=outer_y_coords[3], x_units='data', text='Disgust (' + str(int(disgust_percent)) + '%)', text_font_style='bold', text_align='right'))
	p.add_layout(Label(x=outer_x_coords[4], y=outer_y_coords[4], x_units='data', text='Trust (' + str(int(trust_percent)) + '%)', text_font_style='bold', text_align='right', text_baseline='middle'))
	p.add_layout(Label(x=outer_x_coords[5], y=outer_y_coords[5], x_units='data', text='Anger (' + str(int(anger_percent)) + '%)', text_font_style='bold', text_align='right', text_baseline='top'))
	p.add_layout(Label(x=outer_x_coords[6], y=outer_y_coords[6], x_units='data', text='Anticipation (' + str(int(anticipation_percent)) + '%)', text_font_style='bold', text_align='center', text_baseline='top'))
	p.add_layout(Label(x=outer_x_coords[7], y=outer_y_coords[7], x_units='data', text='Fear (' + str(int(fear_percent)) + '%)', text_font_style='bold', text_align='left', text_baseline='top'))

	# The emotion with the highest number of tweets associated with it (must be cast to a float to avoid integer truncation 
	# in the following co-ordinate calculations).
	max_emotion_count = float(max(emotions.values()))

	# If the max number of tweets associated with any particular emotion is 0 (i.e no tweets have been associated with any emotions) then
	# return the unpopulated graph.
	if max_emotion_count == 0:
			show(p)
	else:
		# The co-ordinates for the patch representing 'positive' emotions.
		positive_x_coords = [(emotions['surprise'] / max_emotion_count) * outer_x_coords[0], (emotions['joy'] / max_emotion_count) * outer_x_coords[2], (emotions['trust'] / max_emotion_count) * outer_x_coords[4], (emotions['anticipation'] / max_emotion_count) * outer_x_coords[6]]
		positive_y_coords = [(emotions['surprise'] / max_emotion_count) * outer_y_coords[0], (emotions['joy'] / max_emotion_count) * outer_y_coords[2], (emotions['trust'] / max_emotion_count) * outer_y_coords[4], (emotions['anticipation'] / max_emotion_count) * outer_y_coords[6]]

		# The co-ordinates for the patch representing 'negative' emotions.
		negative_x_coords = [(emotions['sadness'] / max_emotion_count) * outer_x_coords[1], (emotions['disgust'] / max_emotion_count) * outer_x_coords[3], (emotions['anger'] / max_emotion_count) * outer_x_coords[5], (emotions['fear'] / max_emotion_count) * outer_x_coords[7]]
		negative_y_coords = [(emotions['sadness'] / max_emotion_count) * outer_y_coords[1], (emotions['disgust'] / max_emotion_count) * outer_y_coords[3], (emotions['anger'] / max_emotion_count) * outer_y_coords[5], (emotions['fear'] / max_emotion_count) * outer_y_coords[7]]

		# Create the patches for both positive and negative emotions.
		p.patch(positive_x_coords, positive_y_coords, alpha=0.2)
		p.patch(negative_x_coords, negative_y_coords, fill_color='red', alpha=0.2)

		show(p)
