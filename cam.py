from flask import Flask
from flask import render_template
import os
app = Flask(__name__)
app.debug = True

@app.route("/")
def cam():
	os.system("fswebcam -r 640x480 --no-banner static/images/webcam.jpg")
	return render_template('cam.html' , pic="now.jpg")