from flask import Flask, request
import json
import zlib
from pymongo import MongoClient
import sys
import urllib
from awsudf import awsTerminate, awsScale

app = Flask(__name__)

@app.route('/distributefunction')
def distributefunction():
    try: 
        return myfunction
    except:
        return 'Error'  

@app.route('/distributeinput')
def distributeinput():
    try:
        return inputList.pop()
    except:
        return 'stop'

@app.route('/contribute', methods=['POST'])
def contribute():
    try:
        data = request.stream.read()
        result = json.loads(zlib.decompress(data))
        db.result.insert(result)
        return 'OK'
    except:
        print sys.exc_info()
        return 'Error'

@app.route('/terminate/<instance_id>')
def terminate(instance_id):
    msg = 'Fairwell {}'.format(instance_id)
    if awsTerminate(instance_id):
        return 'Fail: ' + msg
    else: 
        return 'Terminated: ' + msg 
 
if __name__ == '__main__':
    inputList = open('myinput.txt', 'r').readlines()
    myfunction = open('myfunction.py', 'r').read()
    client = MongoClient('localhost', 27017)
    db = client.result
    app.debug = True
    app.run(host='0.0.0.0')
