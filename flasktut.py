from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def get_root():
	maxvalue=10000
	randnumber=random.randint(0,maxvalue)

	return render_template('index.html', maxvalue=maxvalue, number=randnumber)

if __name__ == "__main__":
	app.run(debug=True, host='192.168.0.41')