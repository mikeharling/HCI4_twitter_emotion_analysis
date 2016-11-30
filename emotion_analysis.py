"""
Analyses the processed tweet tokens and tries to match them
to each emotion dictionary
"""

anger_file = open("dictionary/anger.txt", "r")
disgust_file = open("dictionary/disgust.txt", "r")
joy_file = open("dictionary/joy.txt", "r")
surprise_file = open("dictionary/surprise.txt", "r")
anticipation_file = open("dictionary/anticipation.txt", "r")
sadness_file = open("dictionary/sadness.txt", "r")
fear_file = open("dictionary/fear.txt", "r")
trust_file = open("dictionary/trust.txt", "r")
positive_file = open("dictionary/positive.txt", "r")
negative_file = open("dictionary/negative.txt", "r")

anger_vocab = anger_file.read().split('\n')
disgust_vocab = disgust_file.read().split('\n')
joy_vocab = joy_file.read().split('\n')
surprise_vocab = surprise_file.read().split('\n')
anticipation_vocab = anticipation_file.read().split('\n')
sandess_vocab = sadness_file.read().split('\n')
fear_vocab = fear_file.read().split('\n')
trust_vocab = trust_file.read().split('\n')
positive_vocab = positive_file.read().split('\n')
negative_vocab = negative_file.read().split('\n')


emotions = {'joy':0,'surprise':0,'anticipation':0,'trust':0,'sadness':0,'fear':0,'anger':0,'disgust':0,'positive':0,'negative':0,}
t_emotions = {'joy':0,'surprise':0,'anticipation':0,'trust':0,'sadness':0,'fear':0,'anger':0,'disgust':0,'positive':0,'negative':0,}

def emotion_analysis(terms_only):
	for emotion in emotions:
	        emotions[emotion] = 0

	for term in terms_only:
	    if term in anger_vocab:
	        emotions['anger'] += 1
	    if term in disgust_vocab:
	        emotions['disgust'] += 1
	    if term in joy_vocab:
	        emotions['joy'] += 1
	    if term in surprise_vocab:
	        emotions['surprise'] += 1
	    if term in anticipation_vocab:
	        emotions['anticipation'] += 1
	    if term in sandess_vocab:
	        emotions['sadness'] += 1
	    if term in fear_vocab:
	        emotions['fear'] += 1
	    if term in trust_vocab:
	        emotions['trust'] += 1
	    if term in positive_vocab:
	        emotions['positive'] += 1
	    if term in negative_vocab:
	        emotions['negative'] += 1

	for emotion in emotions:
	    t_emotions[emotion] += emotions[emotion]

def get_total_emotions():
	return t_emotions

def print_emotions(total_tweets):
	print "Total Tweets: ", total_tweets, "\n"
	print "Anger: ", t_emotions['anger'], 
	print "Disgust: ", t_emotions['disgust'], 
	print "Joy: ", t_emotions['joy'], 
	print "Surprise: ", t_emotions['surprise'], 
	print "Anticipation: ", t_emotions['anticipation'], 
	print "Sadness: ", t_emotions['sadness'], 
	print "Fear: ", t_emotions['fear'], 
	print "Trust: ", t_emotions['trust'], 
	print "Positive: ", t_emotions['positive'], 
	print "Negative: ", t_emotions['negative']