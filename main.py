'''
This is the main module for flask application.
'''
import os
from flask import Flask,render_template,send_from_directory,request


app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def main():
	if request.method == 'POST':
		print "Post Method"
		temp = request.form['quote_text']
		print "DATA: \n",temp
		return render_template('index.html')

	elif request.method == 'GET':
		print "Get Method"
		return render_template('index.html')
	
	else:
		print "Incorrect Method"		
 
if __name__ == "__main__":
    app.run()