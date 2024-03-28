import json
import logging

from flask import Flask, request
from datetime import datetime


app = Flask(__name__)


# Log
logging.basicConfig(filename="./log/worker.log", level=logging.INFO)


# Returns a message that is working
@app.route('/', methods=['GET'])
def info():
    print( json.dumps( {"status": True, "message": "Working..."} ) )
    logging.info( datetime.now().strftime('%Y-%m-%d_%H:%M:%S') +' - '+ json.dumps( {"status": True, "message": "Working..."} ) )
    return json.dumps( {"status": True, "message": "Working..."} )


# Customizes 404
@app.errorhandler(404)
def page_not_found(e):
    print( json.dumps( {"status": False, "message": "Resource not found"} ) )
    logging.info( datetime.now().strftime('%Y-%m-%d_%H:%M:%S') +' - '+ json.dumps( {"status": False, "message": "Resource not found"} ) )
    return json.dumps( {"status": False, "message": "Resource not found"} ), 404