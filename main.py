from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/queryaddress')
def queryaddress():
    return render_template('queryaddress.html')

@app.route('/village')
def village():
    return render_template('village.html')

@app.route('/highway')
def highway(name=None):
    return render_template('highway.html')


if __name__ == '__main__':
    app.run()