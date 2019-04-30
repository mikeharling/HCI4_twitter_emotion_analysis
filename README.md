# HCI4_twitter_emotion_analysis
A Twitter Emotion Analysis and Visualizations for HCI4 Project

#### Usage

- Copy repo
- Create new virtualenv if wanted (virutalenv my_virtualenv)
- Install dependencies from requirements.txt (pip install -r requirements.txt)
	- Note: May need to install python-dev for wordcloud e.g. 'sudo apt-get instal python-dev' for python2 or 'python3-dev' for python3
- Create a config.py file at root directory containing your Twitter consumer and access keys. See twitter_crawler.py for attributes and Google 'Twitter Access Token' for more info.
- Run server (python server.py)
- Navigate to localhost:5000 in browser
- Enter search query
