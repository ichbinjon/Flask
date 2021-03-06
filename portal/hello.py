import requests
import os
import math
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

#TODO: convert float arithmetics to simpler python3 implicit way
@app.route('/getDuration')
def getDuration():
	mynumber = int(request.args['number'])
	unit = request.args['duration']
	eps = int(request.args['episodes'])

	if unit == 'days':
		number_of_episodes = math.ceil((float(eps) / float(mynumber)))
		done_in = math.ceil((float(eps) / float(number_of_episodes)))

	elif unit == 'weeks':
		number_of_episodes = math.ceil((float(eps) / float(mynumber)))
		done_in = math.ceil((float(eps) / float(number_of_episodes)))

	elif unit == 'months':
		number_of_episodes = math.ceil((float(eps) / float(mynumber)))
		done_in = math.ceil((float(eps) / float(number_of_episodes)))

	elif unit == 'years':
		number_of_episodes = math.ceil((float(eps) / float(mynumber)))
		done_in = math.ceil((float(eps) / float(number_of_episodes)))
	else:
		pass
	return jsonify(number_of_episodes = number_of_episodes, done_in=done_in, unit=unit)

@app.route('/getShowInfo')
def getShowInfo():
	mID = request.args["movieID"]
	return redirect(url_for('TV',movieID = mID))

@app.route('/tv/<string:movieID>')
def TV(movieID):
	apiKey = os.environ.get('PORTAL_API')
	info = {'api_key':apiKey, 'language':'en-US'}
	data=requests.get(' https://api.themoviedb.org/3/tv/'+ movieID,params=info)
	data=data.json()
	name = data["name"]
	numEps = data["number_of_episodes"]
	numSeasons = data["number_of_seasons"]
	return render_template('movie.html', data=data,numSeasons=numSeasons, numEps=numEps, name=name)	
	

@app.route('/test')
def test():
	return redirect('http://www.google.com',302)