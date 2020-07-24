from flask import Flask, render_template, Markup

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('l_template.html', value='<h1> Hey jude </h1>')

@app.route('/home')
def home():
    value = Markup('<h2>THis is markup object for autoescaping off, enable html externally. </h2>')
    return render_template('l_template.html', value=value)
