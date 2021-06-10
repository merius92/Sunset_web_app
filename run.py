from flask import Flask, redirect, url_for, render_template, jsonify
import numpy as np
from script_web import *

app = Flask(__name__, template_folder='templates')

random_dec = np.random.rand()


@app.route('/updatemetar', methods=['POST'])
def updatemetar():
	random_dec = np.random.rand()
	report_metar = Metar(aerodrome, report)
	sunset = data["ss"][day - 1] 
	return jsonify('', render_template('metar.html', aerodrome=aerodrome, report_metar=report_metar, day_night=day_night, vmc_imc=vmc_imc, sunset=sunset, random_dec=random_dec))

@app.route("/")
def home():
	return render_template('index.html', aerodrome=aerodrome, report_metar=report_metar, vmc_imc=vmc_imc, day_night=day_night, random_dec=random_dec, sunrise=sunrise, sunset=sunset)

if __name__ == "__main__":
	app.run(debug=True)