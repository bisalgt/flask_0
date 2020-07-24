from flask import Flask, render_template, Markup

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('l_template.html', value='<h1> Hey jude </h1>')

@app.route('/home')
def home():
    value = Markup('<h2>THis is markup object for autoescaping off, enable html externally. </h2>')
    return render_template('l_template.html', value=value)

@app.template_filter('capitalize')
def capitalize_data(value):
    return value.upper()


def lower_value(val):
    return f'{val.lower()} hello there lower value'
app.jinja_env.filters['lower'] = lower_value 



@app.context_processor
def myname():
    return {'name':'Bishal Gautam', 'age':24}
