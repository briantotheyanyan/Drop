from flask import request,Flask,render_template, url_for,redirect,request,make_response
from time import gmtime, strftime
import urllib2,json
import database


app = Flask(__name__)
app.secret_key = "secret"

Latitude = 0
Longitude = 0

@app.route('/', methods=['GET', 'POST'])
def main():
	if request.method == 'GET':
		return render_template('Login.html')
	else:
		if request.form['button'] == 'login':
			if database.verifyAccount(request.form['username'],request.form['password']):
				username = request.form['username']
				Latitude = request.form['Latitude']
				Longitude = request.form['Longitude']
				resp = make_response(redirect(url_for('home')))
				resp.set_cookie('username', username)
				resp.set_cookie('Longitude', Longitude)
				resp.set_cookie('Latitude', Latitude)
				return resp
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
	
   	if request.method == 'GET':
                username = request.cookies.get('username')
		Latitude = request.cookies.get('Latitude')
		Longitude = request.cookies.get('Longitude')
		MessageList = database.returnAllMessages()
		mymessages = database.returnMessagesbyUser(username)
		messages = database.returnMessagesinRange(Latitude,Longitude)
		names = database.returnNamesinRange(Latitude,Longitude)
		time = database.returnTimeinRange(Latitude,Longitude)
		
		return render_template("Home.html", MessageList=MessageList, messages=messages, Latitude=Latitude, Longitude=Longitude, names = names, time =time, username=username, mymessages = mymessages)   		
	else:
		button = request.form["button"]
		if button == 'Create Message':
			newM = request.form['line']
			Latitude = request.form['Latitude']
			Longitude = request.form['Longitude']
			time = strftime("%a, %b %d, %Y %I:%M:%S %p %Z", gmtime())
			username = request.cookies.get('username')
			resp = make_response(redirect(url_for('home')))
			resp.set_cookie('Longitude', Longitude)
			resp.set_cookie('Latitude', Latitude)
			if newM:
				database.writeMessage(newM,float(Longitude),float(Latitude),username, time)
			return resp
		elif button == "Logout":
			page = ""
			username = ""
			return redirect(url_for('main'))




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
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(port=5000)
