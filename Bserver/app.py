from flask import Flask, request, jsonify
import requests
import json
from templates import Connector

app = Flask(__name__)

#direction_code = requests.post('http://localhost:7777','303')

@app.route('/bbb', methods=['POST','GET'])
def B_rasp():
    if request.method == 'POST':
        try:
            data = json.loads(request.data)
            return json.dumps(data)
        #Connector.serial_connection(dataDict["code_num"])
        except:
            HaveError = {'code_num': 555}
            res = requests.post('http://localhost:3333/checking', json.dumps(HaveError))
            return HaveError['code_num']

if __name__ == '__main__':
    app.run(host='localhost', port='4444', debug = False)
