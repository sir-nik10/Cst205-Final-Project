#jose Flores 
#professor Wes Modes
#CST205
#May 11, 2020

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def hello():
	return render_template('cvwebpage.html')