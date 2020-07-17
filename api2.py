from flask import Flask, make_response


app = Flask('api2')

def func(*args, **kwargs):
    print(args, kwargs)
    print(dir(args))
    return args


@app.route('/')
# @app.after_request(func)
def index():
    resp = make_response('hey there')
    return resp

