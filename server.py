from flask import Flask
from flask import render_template
from twitter_crawler import search
app = Flask(__name__)

@app.route('/search')
@app.route('/search/<search_term>')
def search_start(search_term):
	search(search_term)
	return render_template('main.html', search_term=search_term)

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/wordclouds')
def wordclouds():
    return render_template('wordclouds.html')

@app.route('/radarscatter')
def radarscatter():
    return render_template('radar_scatter.html')

@app.route('/patches')
def patches():
    return render_template('patches.html')

@app.route('/barchart')
def barchart():
    return render_template('horizontal-bar-single.html')

if __name__ == '__main__':
    app.run()