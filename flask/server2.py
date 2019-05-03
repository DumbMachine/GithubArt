#!flask/bin/python
from flask import Flask, jsonify
from flask import request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api', methods=['GET'])
def get_tasks():
    return jsonify(request.args.get('data'))


@app.route('/test/', methods=['GET','POST'])
@cross_origin()
def test():
    
    if request.method == "GET":
        print("GET")
        return "GEtting"
    clicked=None
    if request.method == "POST":
        print("POST")
        clicked=request.data
        print("clicked; ", clicked)
    return "."

if __name__ == '__main__':
    app.run(port="5001",debug=True)