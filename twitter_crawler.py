import tweepy
from tweepy import OAuthHandler
import json
import re
import string
import math
import random
import numpy as np
from PIL import Image
from collections import Counter
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from wordcloud import WordCloud
from emotion_analysis import emotion_analysis, print_emotions, get_total_emotions
from polarScatterChart import plotPolarScatterChart
from pos_neg_pie import pos_neg_pie
from horizontal_bar_single import horiz_bar_single
from emotion_visualiser import emotion_visualiser
import config
 
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_secret = config.access_secret
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
tknz = TweetTokenizer()

count_all = Counter()

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
    r'https://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
        
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def process_or_store(tweet):
    print(json.dumps(tweet))


 
def tokenize(s):
	return tknz.tokenize(s)
    #return tokens_re.findall(s)
 
def preprocess(s, lowercase=True):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

def testFunc():
    print testing

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(40, 60)

"""
Twitter search function.  Each api.search() returns max 100 results,
adjust the amount of results (and writes) to crawl more.
"""
def search(search_query):
    print "Searching for " + search_query
    #search_query = "glasgow city council"
    results = api.search(q=search_query, count=100)
    results.sort(key=id)
    highest = results[len(results) - 1].id
    results2 = api.search(q=search_query, count=100, max_id=highest)
    """
    results2.sort(key=id)
    highest = results[len(results2) - 1].id
    results3 = api.search(q=search_query, count=100, max_id=highest)
    highest = results[len(results3) - 1].id
    results4 = api.search(q=search_query, count=100, max_id=highest)
    highest = results[len(results4) - 1].id
    results5 = api.search(q=search_query, count=100, max_id=highest)
    """
    with open('mytweets.json', 'w') as f:
        for result in results:
            f.write(json.dumps(result._json)+"\n")
        for result in results2:
            f.write(json.dumps(result._json)+"\n")
    """
        for result in results3:
            f.write(json.dumps(result._json)+"\n")
        for result in results4:
            f.write(json.dumps(result._json)+"\n")
        for result in results5:
            f.write(json.dumps(result._json)+"\n")
    """

    """
    Stop words
    """
    punctuation = list(string.punctuation)
    stop = stopwords.words('english') + punctuation + ['rt', 'via', 'en', 'de', 'el', 'glasgow', search_query]

    """
    Tweet processing
    """
    total_tweets = 0
    com = defaultdict(lambda : defaultdict(int))
    fname = 'mytweets.json'
    with open(fname, 'r') as f:        
        print "Performing emotional analysis..."
        for line in f:            
            total_tweets += 1
            tweet = json.loads(line)
            tweet = tweet['text'].encode('utf-8')
            terms_only = [term for term in preprocess(tweet) 
                      if term not in stop 
                      and not term.startswith(('@', 'https', '.'))]

            emotion_analysis(terms_only)
            t_emotions = get_total_emotions()
            count_all.update(terms_only)
    print "Emotional analysis done"
    print "Creating wordclouds..."
    wordcloud()
    print "Wordclouds done"
    #print_emotions(total_tweets)
    #print(count_all.most_common(100))
    print "Total Tweets: " + str(total_tweets)
    plotPolarScatterChart(t_emotions, search_query, total_tweets)
    pos_neg_pie(t_emotions)
    horiz_bar_single(t_emotions, search_query)
    emotion_visualiser(t_emotions, search_query)

"""
Wordcloud creation
"""
def wordcloud():
    with open('wordcloud.txt', 'w') as cloud:
        for term, value in count_all.most_common(150):
            for i in range(value):
                cloud.write(term.encode('ascii', 'ignore') + " ")

    alice_coloring = np.array(Image.open("masks/alice_color.png"))
    stormtrooper = np.array(Image.open("masks/stormtrooper_mask.png"))
    text = open('wordcloud.txt').read()

    wordcloud = WordCloud(background_color="white", max_words=2000, max_font_size=60, width = 700,height= 500,).generate(text)
    image = wordcloud.to_image()
    image.save('static/wordclouds/default.png')

    wordcloud = WordCloud(background_color="white", max_words=2000, mask=alice_coloring, max_font_size=60).generate(text)
    image = wordcloud.to_image()
    image.save('static/wordclouds/alice.png')

    wordcloud = WordCloud(background_color="white", max_words=2000, mask=stormtrooper, max_font_size=60).generate(text)
    wordcloud.recolor(color_func=grey_color_func, random_state=3)
    image = wordcloud.to_image()
    image.save('static/wordclouds/stormtrooper.png')

