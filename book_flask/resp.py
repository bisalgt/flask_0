from flask import Flask
from flask import request
from flask import redirect, abort
app = Flask(__name__)


@app.route('/')
def index():
    # print(dir(request))
    # print(request.headers)
    # return f'the header is {request.headers}', 200, {'header1': 'value'}
    return redirect('http://127.0.0.1:5000/name')

@app.route('/name')
def name():
    return 'Name page'

@app.route('/name/<int:id>')
def chk_id(id):
    if id%2==0:
        abort(404)
    return 'id is not divisible by 2'


