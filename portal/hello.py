import requests
import os
from flask import Flask, render_template, request, jsonify, redirect, url_for
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
	info = {'api_key':apiKey, 'query':text, 'language':'en-US'}
	data=requests.get(' https://api.themoviedb.org/3/search/tv',params=info)
	data=data.json()
	#data = jsonify(result=1+2)
	return jsonify(data)

@app.route('/getShowInfo')
def getShowInfo():
	mID = request.args["movieID"]
	return redirect(url_for('TV',movieID = mID))

@app.route('/tv/<movieID>')
def TV(movieID):
	apiKey = os.environ.get('PORTAL_API')
	info = {'api_key':apiKey, 'language':'en-US'}
	data=requests.get(' https://api.themoviedb.org/3/tv/'+ movieID,params=info)
	data=data.json()
	return render_template('movie.html', data=data)

@app.route('/test')
def test():
	return redirect('http://www.google.com',302)