from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    li = [1,2,3,4]
    return render_template('base.html', digits=li)


@app.route('/derive')
def derived():
    li = [2,3,4,5]
    return render_template('derived.html', digits=li)
