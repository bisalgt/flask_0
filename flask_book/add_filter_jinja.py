from flask import Flask, render_template

app = Flask(__name__)


@app.template_filter('capitalizer')
def capitalize(a):
    return a.capitalize()


def upperize(a):
    return a.upper()

app.jinja_env.filters['upperize'] = upperize


@app.route('/')
@app.route('/<name>')
def index(name='Bishal'):
    return render_template('apply_filter.html', name=name)
