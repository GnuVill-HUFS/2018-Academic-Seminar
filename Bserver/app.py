from flask import Flask, request, jsonify
import requests
import json
from raspToSerial.haksuljae import serial_connection

# from templates import Connector

A_SERVER = 'http://192.168.1.4:3333'
B_SERVER = 'http://192.168.1.5:4444'

app = Flask(__name__)


# direction_code = requests.post('http://localhost:7777','303')

@app.route('/bbb', methods=['POST', 'GET'])
def B_rasp():
    if request.method == 'POST':
        try:
            try:
                data = json.loads(request.data.decode('utf-8'))
            except:
                return
            print('before_ard')

            print('ard_connectVal')
            result = serial_connection(data['code_num'])
            # bbb로 넘어오면 서버가 serial 연결.
            print('result')
            return result

        except:
            result = serial_connection(data['code_num'])
            # bbb로 넘어오면 서버가 serial 연결.
            print('result')
            return result
            HaveError = {'code_num': 555}
            res = requests.post(A_SERVER + '/checking', json.dumps(HaveError))
            return HaveError['code_num']
    else:
        return "THIS IS GET"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4444', debug=False)

