from flask import request,Flask,render_template, url_for,redirect,request
import urllib2,json
import database

app = Flask(__name__)
#app.secret_key = "secret"


Latitude = 0
Longitude = 0

@app.route('/', methods=['GET', 'POST'])
def main():
	global username
	if request.method == 'GET':
		return render_template('Login.html')
	else:
		if request.form['button'] == 'login':
			if database.verifyAccount(request.form['username'],request.form['password']):
				username = request.form['username']
				return redirect(url_for('home'))
			else:
				return redirect(url_for('main'))
		elif request.form['button'] == 'register':
			return redirect(url_for('register'))
@app.route('/register',methods=['GET','POST'])
def register():
	if request.method == 'GET':
		   return render_template('Register.html')
	else:
		if request.form['button'] == 'register':
			if database.verifyAccount(request.form['username'],request.form['password']):
				return redirect(url_for('register'))
			else:
				database.createAccount(request.form['username'],request.form['password'],[request.form['BirthMonth'],request.form['Birthday'],request.form['BirthYear']])
				return redirect(url_for('main'))

@app.route('/home', methods=['GET', 'POST'])
def home():
	global username
	global Longitude
	global Latitude
   	if request.method == 'GET':
		if  request.form['Latitude'] != None:
			Latitude = request.form['Latitude']
			Longitude = request.form['Longitude']
		messages = database.returnMessagesinRange(Latitude,Longitude)
		return render_template('Home.html', messages=messages, Latitude = Latitude, Longitude = Longitude)
		if button == 'Create Message':
			newM = request.form['line']
			if newM:
				database.writeMessage(newM,float(Longitude),float(Latitude),username)


'''@app.route('/scan', methods=['GET', 'POST'])
def scan():
	global username
	global Longitude
	global Latitude

    	if request.method == 'GET':
		
    			messages = database.returnMessagesinRange(Latitude,Longitude)
    			return render_template('SCAN.html',messages=messages, Latitude = Latitude, Longitude = Longitude)
	else:
    		button = request.form['button']
#_______________________________________________________________SCAN page has "Back" button
    		if button == 'BACK':
			mode = ""
			return redirect(url_for('home'))		





@app.route('/new', methods=['GET', 'POST'])  		   
def new():
	global username
	global Longitude
	global Latitude

    	if request.method == 'GET':	
		return render_template('NEW.html', Latitude = Latitude, Longitude = Longitude)
	else:
    		button = request.form['button']
#_______________________________________________________________NEW page has "Create Message" and "Cancel" buttons
		if button == 'Create Message':
			newM = request.form['line']
			if newM:
				database.writeMessage(newM,float(Longitude),float(Latitude),username)
				return redirect(url_for('home'))
			return redirect('/new')

		elif button == 'Cancel':
			return redirect(url_for('home'))

@app.route('/maps', methods=['GET', 'POST'])  		   
def maps():
	if request.method == 'GET':
		MessageList = database.returnAllMessages()
		return render_template('testing-map.html', MessageList = MessageList)'''


if __name__=="__main__":
    app.debug=True
    app.run(port=5000)
