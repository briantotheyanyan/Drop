from flask import request,Flask,render_template, url_for,redirect,request
import urllib2,json
import database

app = Flask(__name__)
#app.secret_key = "secret"





@app.route('/', methods=['GET', 'POST'])
def main():
	global mode
    	if request.method == 'GET':
		return render_template('GPS.html',mode = mode)
	else:
    		button = request.form['button']
#_______________________________________________________________Main page has "Scan" and "New" buttons

    		if button == 'BACK':
			mode = ""
			return redirect('/')






@app.route('/scan', methods=['GET', 'POST'])
def scan():
	global mode
    	if request.method == 'GET':
    		
    			Latitude = request.form['Latitude']
			Longitude = request.form['Longitude']
    			messages = database.returnMessagesinRange(Latitude,Longitude)
    			return render_template('GPS.html',messages=messages, mode = mode)
	else:
    		button = request.form['button']
#_______________________________________________________________SCAN page has "Back" button
		if button == button == 'SCAN':
			mode = "SCAN"
			return redirect('/')

		elif button == 'NEW':
			mode = "NEW"
			return redirect('/')









@app.route('/new', methods=['GET', 'POST'])  		   
def new():    		
       	global mode
    	if request.method == 'GET':	
		return render_template('GPS.html',mode = mode)
	else:
    		button = request.form['button']
#_______________________________________________________________NEW page has "Create Message" and "Cancel" buttons
		if button == 'Create Message':
			newM = request.form['line']
			Latitude = request.form['Latitude']
			Longitude = request.form['Longitude']
			if newM:
				writeMessage(newM,Longitude,Latitude)
				mode = ""
			return redirect('/')

		elif button == 'Cancel':
			mode = ""
			return redirect('/')






if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0')
