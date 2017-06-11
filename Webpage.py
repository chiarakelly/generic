from flask import Flask, render_template, request
import requests

app= Flask(__name__)
#This displays temperature
@app.route('/temperature', methods=['POST'])
#Function temperature
def temperature():
	return render_template('temperature.html')

@app.route('/')
def index(): 
	return render_template('index.html')
	
if __name__== '__main__':
	app.run(debug=True)
