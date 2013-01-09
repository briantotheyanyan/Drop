from flask import request,Flask,render_template, url_for,redirect,request
import urllib2,json
import database

app = Flask(__name__)
#app.secret_key = "secret"
name = ""

@app.route('/', methods=['GET', 'POST'])
def check():
	latitude=request.args.get('latitude','-1')
	latitude=request.args.get('latitude','-1')
#	database.returnMessagesinRange(longitude,latitude)

@app.route("/write")
def write():
	latitude=request.args.get('latitude','-1')
	latitude=request.args.get('latitude','-1')
	text = request.form['text']
	database.writeMessage(text,longitude,latitude):
	return True

@app.route("/register")
def register():
	username=request.args.get('username','')
	password=request.args.get('password','')
	birthday=request.args.get('birthday','')
	database.createAccount(username,password,birthday):
	 return "True"
	
if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0')
