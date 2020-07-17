from flask import Flask

app = Flask('api1')


#@app.route('/')
def index():
    return 'index Page'


app.add_url_rule('/', 'index',)
app.view_functions['index'] = index
