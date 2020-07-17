from flask import Flask

app = Flask(__name__)

def func():
    print('function is called')


@app.route('/')
def index():
    return 'hey jude'


app.before_first_request(func)
