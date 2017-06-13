from flask import Flask 
from flask import render_template
from flask import request
from flask import json
import requests 
from flask import Webpage
	

app = Flask("MyApp")

@app.route("/")
def index():
	result = {'result': 'Go outside'}
	result = json.jsonify(result)
	return result

@app.route('/result/', methods=['POST'])
def hello():
	temp_c=request.form['postcode']
	if postcode == "se38bs":result = {'result': 'Go outside'}
	else:
		result = {'result': 'Go inside'}
	result = json.jsonify(result)
	return result



	app.run()