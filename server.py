from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hey! I am the Chat server api!"


@app.route('/hello')
def hello():
    return "<h1>Hello world!</h1>"