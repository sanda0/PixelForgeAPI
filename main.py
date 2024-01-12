from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

  # /?img=abc.png&w=100&h=100&b=1


@app.route('/image', methods=['GET'])
def image():
    img = request.args.get('img')
    w = request.args.get('w')
    h = request.args.get('h')
    b = request.args.get('b')
    return "image"
