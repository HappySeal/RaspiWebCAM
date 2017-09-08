from flask import Flask
from flask import render_template
import os
app = Flask(__name__)
app.debug = True

@app.route("/")
def cam():
	os.system("fswebcam -r 640x480 --no-banner static/images/webcam.jpg")
	return render_template('cam.html' , pic="static/images/webcam.jpg")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)