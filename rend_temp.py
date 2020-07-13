from flask import render_template
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    print(dir(request))
    print(request.args)
    return render_template('home.html', name=name)
