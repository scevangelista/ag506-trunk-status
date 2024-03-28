import json
import logging

from datetime import datetime
from flask import Flask, request
from worker import getData


app = Flask(__name__)


# Log
logging.basicConfig(filename="./log/worker.log", level=logging.INFO)
dformat = '%Y-%m-%d_%H:%M:%S'


# Collects the data
@app.route('/collect', methods=['POST'])
def collect():
    if request.method == 'POST':

        request_json = request.get_json()
        url = request_json.get('url')
        user = request_json.get('user')
        passw = request_json.get('password')

        res = getData(url, user, passw)
        print(json.dumps(res))
        logging.info(datetime.now().strftime(dformat)+' - '+json.dumps(res))

        if res['status'] == True:
            return json.dumps(res), 200
        else:
            return json.dumps(res), 500


# Returns a message that is working
@app.route('/', methods=['GET'])
def info():
    print(json.dumps({"status": True, "message": "Working..."}))
    logging.info(datetime.now().strftime(dformat)+' - '+json.dumps({"status": True, "message": "Working..."}))
    return json.dumps({"status": True, "message": "Working..."})


# Customizes 404
@app.errorhandler(404)
def page_not_found(e):
    print(json.dumps({"status": False, "message": "Resource not found"}))
    logging.info(datetime.now().strftime(dformat)+' - '+json.dumps({"status": False, "message": "Resource not found"}))
    return json.dumps({"status": False, "message": "Resource not found"}), 404
