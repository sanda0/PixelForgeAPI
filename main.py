from flask import Flask, after_this_request, request,send_from_directory,redirect
from func.resize import Resize
import os
app = Flask(__name__)


@app.route('/')
def hello():
    return """
  <p>Hello, World!</p>
  <img src="/image?img=test1.jpg&w=400&h=400">
  """

  # /?img=abc.png&w=100&h=100&b=1


@app.route('/image', methods=['GET'])
def image():
    img = request.args.get('img')
    w = request.args.get('w')
    h = request.args.get('h')
    b = request.args.get('b')
    
    if img != "":
      new_file = ""
      if w != "" and h != "":
        resize = Resize(img, int(w), int(h))        
        new_file = resize.execute()
        return redirect('/file/'+new_file)

    
    return "null"


@app.route('/file/<path:path>')
def serve_file(path):
    @after_this_request
    def remove_file(response):
      try:
        os.remove('output/'+path)
      except:
        pass
      return response
    return send_from_directory('output',path)
  
