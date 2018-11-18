from flask import Flask, request, jsonify
import requests
import json
from raspToSerial.haksuljae import Connector as ard_cn
#from templates import Connector

A_SERVER = 'http://192.168.0.2:3333'
B_SERVER = 'http://192.168.0.5:4444'

app = Flask(__name__)

#direction_code = requests.post('http://localhost:7777','303')

@app.route('/bbb', methods=['POST','GET'])
def B_rasp():
    if request.method == 'POST':
        try:
            data = json.loads(request.data)

            ard_connectVal = ard_cn()
            result = ard_connectVal.serial_connection(data['code_num'])
            # bbb로 넘어오면 서버가 serial 연결.
            return result

        except:
            HaveError = {'code_num': 555}
            res = requests.post(A_SERVER + '/checking', json.dumps(HaveError))
            return HaveError['code_num']
    else:
        return "THIS IS GET"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4444', debug = False)
