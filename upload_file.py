from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        return 'hello'
    else:
        return render_template('home.html')
