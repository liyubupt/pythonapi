import sys
import os
from flask import Flask, jsonify
from flask_restful import reqparse, Api, Resource
from apispec.ext.marshmallow import MarshmallowPlugin
from marshmallow import Schema, fields
import json
import pyodbc
from apispec import APISpec
from flasgger import Swagger
import logging

# This is a simplified example that only support GET request.
# It is meant to help you to get you started if you're new to development
# and to show how simple is using Azure SQL with Python
# A more complete example is in "app.py"
# To run this simplified sample follow the README, but instead of running "flask run"
# just run "python ./simple-app.py"
# Enjoy!

# Initialize Flask
app = Flask(__name__)
swagger = Swagger(app)

app.config['SWAGGER'] = {
    'title': 'My API',
    'uiversion': 3
}

# Setup Flask Restful framework
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('customer')

# Create connection to Azure SQL
conn = pyodbc.connect(os.environ['SQLAZURECONNSTR_WWIF'])

@app.route('/customer/<customer_id>')
def get(customer_id): 
    """Example endpoint returning a list of colors by palette
    This is using docstrings for specifications.
    ---
    parameters:
      - name: customer_id
        in: path
        type: string
        required: true
        default: all
    responses:
      200:
        description: customer
    """    
    cursor = conn.cursor()    
    logging.warning(customer_id) 
    cursor.execute("select * from web.Claim where ID = ?", customer_id)
    #result = json.loads(cursor.fetchone()[0])     
    result = cursor.fetchone()
    logging.warning(result) 
    cursor.close()
    return jsonify(
        {"ID": result[0], "Claim": result[1], "ChangeType": result[2], "PublicID": result[3]}
    ), 201


# Start App
if __name__ == '__main__':
    app.run()