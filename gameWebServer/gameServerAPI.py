from flask import Flask, request, jsonify, make_response
from flask_socketio import SocketIO

app = Flask(__name__)

@app.route('/secretMessage')
def secretMessage():
    return '<p>yes</p>'

# @app.route('/secretMessage/', methods = ['POST', 'OPTIONS'])
# def helloWorld():
#     if request.method == "OPTIONS": # CORS preflight
#         return _build_cors_preflight_response()
#     elif request.method == "POST": # The actual request following the preflight
#         return _corsify_actual_response('<p>Hello World</p>')
#     else:
#         raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))

# ugly CORS hack
def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response
def _corsify_actual_response(response):
    corsifiedResponse = jsonify(response)
    corsifiedResponse.headers.add("Access-Control-Allow-Origin", "*")
    return corsifiedResponse

def run():    
    app.run()
