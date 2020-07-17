from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.cookies)
        print(request.files)
        return request.form
    else:
        return render_template('home.html')


@app.errorhandler(404)
def page_not_found(error):
    return error
    
