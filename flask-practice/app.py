from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'


@app.route('/time')
def get_time():
    return render_template(f'time.html', local_time=datetime.now())


if __name__ == '__main__':
    app.run(debug=True)
