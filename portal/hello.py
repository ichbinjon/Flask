import requests
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/new/')
def hello_new():
	data=requests.get('https://api.themoviedb.org/3/discover/movie?api_key=6d64a72486b47e66eaf157cafc5a0860&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1')
	data=data.json()
	return render_template('new.html',data=data)