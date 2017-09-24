import requests
import os
from flask import Flask, render_template, request, jsonify
#API Keys are taken from OS environment!
app = Flask(__name__)

@app.route('/')
def hello_new():
	apiKey = os.environ.get('PORTAL_API')
	data=requests.get('https://api.themoviedb.org/3/discover/movie?api_key='+apiKey+'&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1')
	data=data.json()
	return render_template('new.html',data=data)

@app.route('/search')
def search():
	text = request.args['searchText']
	apiKey = os.environ.get('PORTAL_API')
	info = {'api_key':apiKey, 'query':text}
	data=requests.get('https://api.themoviedb.org/3/search/movie',params=info)
	data=data.json()
	#data = jsonify(result=1+2)
	return jsonify(data)

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)