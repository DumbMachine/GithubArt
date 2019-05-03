#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Another useless python script
@author: ratin
"""
#TODO: Implement Authentication System
#TODO: Implement feature to save in Mongo the books which are asked often
#TODO: Implement feature to ask for the number of books sent in the API

import datetime
import sys
from json import dumps

from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# api = Api(app , errors={
#     'NotFound': {
#         'message': "Something is missing.",
#         'status': 404,
#         }
#     }
# )

# class Serve(Resource):
#     def __init__(self,book_type="novel"):
#         self.message= "Working"
#         self.git_name = request.args.get("git_name")
#         self.git_email = request.args.get("git_email")
#         self.data = request.args.get('data')
#         self.error = None

#     def do(self):
#         from Art import GithubArt
#         self.message = "done"
#         temp = GithubArt(self.git_email,self.git_name)
#         temp.cnv_DataURL_image(self.data)
#         temp.cleanup()
#         # self.message = temp.everything()
#         # temp.finish()


#     def get(self):
#         self.do()
#         print("==================")
#         print(self.data)
#         print("==================")
#         print(type(self.data))
#         if self.error:
#             return {
#                 "error": self.error,
#                 "data" : "",
#                 'name' : "",
#                 'email': "",
#                 "error": "",
#                 "time": str(datetime.datetime.now())[:]
#             }
#         else:
#             return {
#                 "data": self.data,
#                 'name': self.git_name,
#                 'email': self.git_email,
#                 "error": self.error,
#                 "time": str(datetime.datetime.now())[:]
#             }


# api.add_resource(Serve, "/api")

@app.route('/test/', methods=['GET','POST'])
@cross_origin()
def test():
    import json

    if request.method == "GET":
        print("GET")
        return "Dont Come here"
    clicked=None
    if request.method == "POST":
        print("POST")
        clicked=request.data

        from Art import GithubArt


        something = json.loads(clicked.decode())
        print("clicked; ", something['name'])
        temp = GithubArt(something["email"], something['name'])
        temp.cnv_DataURL_image(something['DataURL'])

        print(temp.everything())
        temp.finish()
        # temp.cleanup()

    return "."


if __name__ == "__main__":
    app.run(port="5002",debug=True)
