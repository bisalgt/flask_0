from flask import Flask, make_response


app = Flask(__name__)


def func(resp):
    print(dir(resp))
    print(resp.response)
    print('inside after req function')
    resp2 = make_response('response changed')
    return resp2


@app.route('/')
def index():
    return 'this is resp'


app.after_request(func)

