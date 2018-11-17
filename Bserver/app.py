from flask import Flask, request, jsonify
import requests
import json
from templates import Connector

app = Flask(__name__)

#direction_code = requests.post('http://localhost:7777','303')

@app.route('/bbb', methods=['POST'])
def B_rasp():
    try:
        dataDict = json.loads(request.data)
        return str(dataDict)
        #Connector.serial_connection(dataDict["code_num"])
    except:
        HaveError = {'word':'Error!!!!', 'code_num': 555}
        res = requests.post('http://localhost:8888/checking', HaveError)
        return HaveError['word']

if __name__ == '__main__':
    app.run(host='localhost', port='7777', debug = True)
