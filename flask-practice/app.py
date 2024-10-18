from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


# Когда пользователь в браузере наберет АДРЕСХОСТА/ (зайдет на главную страницу сайта), вызывается эта функция
@app.route('/')
def home():
    return 'Hello, World!'


# Когда пользователь в браузере наберет АДРЕСХОСТА/greet/любое-значение, вызывается эта функция и передаёт в переменную name значение, указанное пользователем после greet/
@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'


# Когда пользователь в браузере наберет АДРЕСХОСТА/time, вызывается эта функция, обработает html страницу, добавив в неё значение переменной local_time, и отправит пользователю
@app.route('/time')
def get_time():
    return render_template(f'time.html', local_time=datetime.now())


if __name__ == '__main__':
    app.run(debug=True)
