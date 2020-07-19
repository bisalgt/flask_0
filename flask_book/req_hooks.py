from flask import Flask

app = Flask(__name__)

# def before(a):
#    print('before')

# def after(a):
#    print('after')

@app.route('/')
@app.route('/user/<int:id>')
# @app.before_request(before)
# @app.after_request(after)
def index(id=None):
    return 'hey there'
