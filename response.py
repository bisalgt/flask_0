from flask import Flask
from flask import make_response
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response(render_template('home.html'))
    print(resp)
    resp.set_cookie('username', 'the username')
    print('----------', resp)
    return resp
