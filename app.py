from flask import request,Flask,render_template, url_for,redirect,request
import urllib2,json
import database

app = Flask(__name__)
#app.secret_key = "secret"
mode = ""

@app.route('/', methods=['GET', 'POST'])
def main():
	global mode
    	if request.method == 'GET':
    		if mode = "SCAN":
    			Latitude = request.form['Latitude']
			Longitude = request.form['Longitude']
    			messages = database.returnMessagesinRange(Latitude,Longitude)
    			return render_template('GPS.html', messages = messages, mode = mode)
    		
		elif mode = "NEW":
			return render_template('GPS.html',mode = mode)
		else:
    			return render_template('GPS.html',mode = mode)
    	else:
    		button = request.form['button']
    		
    		if button == 'BACK':
			mode = ""
			return redirect('/')
		elif button == 'Create Message':
			newM = request.form['title']
			Latitude = request.form['Latitude']
			Longitude = request.form['Longitude']
			if newM:
				writeMessage(newM,Longitude,Latitude):
				mode = ""
			return redirect('/')
		elif button == 'Cancel':
			mode = ""
			return redirect('/')
		elif button == 'SCAN':
			mode = "SCAN"
			return redirect('/')
		elif button == 'NEW':
			mode = "NEW"
			return redirect('/')
  		   
    		
    		


if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0')