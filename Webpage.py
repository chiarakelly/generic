from flask import Flask, render_template, request
import requests


app = Flask(__name__)
#This displays temperature
@app.route('/temperature', methods=['POST'])
#Function temperature
def temperature():
	Postcode = request.form['Postcode']
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+Postcode+',GB&appid=c7b7a885c9ec2fb1796372260766f368')
	json_object = r.json()
	#Refer to search page 'main'
	temp_k = float(json_object['main']['temp'])
	temp_c = (temp_k - 273.15)
	if temp_c >= 20: 
		return render_template('hot.html', temp=temp_c)
	else: 
		return render_template('cold.html', temp=temp_c)

@app.route('/')
def index(): 
	return render_template('index.html')

if __name__== '__main__':
	app.run(debug=True)