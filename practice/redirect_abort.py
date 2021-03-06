from flask import abort, redirect, url_for
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()

@app.errorhandler(404)
def error_handler_func(error):
    print(error)
    return 'error'
