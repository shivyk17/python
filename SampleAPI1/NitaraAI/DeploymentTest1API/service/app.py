# -*- coding: utf-8 -*-
"""
Created on Thu May 20 14:24:19 2021

@author: Deepa.Mohite
"""

"""
Provide an implementation for the Straw Data Reader API.
The APIs accept the straw image as input and gives the text as output.

Accepts
-------
It accepts image as input.

Returns
-------
Text found in image, or proper message if text is not found.
       
There are 2 APIs.
1) Without saving the uploaded image
2) By saving the uploaded image

"""

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

import configparser

from .stream import DeploymentTestStream
from .upload import DeploymentTestUpload

config = configparser.ConfigParser()
config.read('config_file.ini')

#: Initialize the required parameters to api
app = Flask(__name__)
app.secret_key = config['AUTHDETAILS']['secrete_key']
app.config['ALGORITHM'] = config['AUTHDETAILS']['algorithm']
app.config['PROPAGATE_EXCEPTIONS'] = config['AUTHDETAILS']['propogate_exceptions'] == "True"
app.config['JWT_IDENTITY_CLAIM'] = config['AUTHDETAILS']['jwt_identity_claim']

jwt = JWTManager(app)
api = Api(app)

api.add_resource(DeploymentTestStream, '/deploymenttest1/stream')
api.add_resource(DeploymentTestUpload, '/deploymenttest1/upload')

@app.route("/", methods=['GET','POST'])
def home():
    return "Hello, This is Straw Data Reader Flask App."

if __name__ == '__main__':
    app.run(port=5000)