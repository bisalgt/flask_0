#! /home/bishal/Projects/flask_project/venv/bin/python 


from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hey'


if __name__=='__main__':
    app.run()