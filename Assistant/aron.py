import requests, json
from flask import jsonify

assist_URL = 'http://localhost:8888/aaron'
serial_URL = 'http://localhost:8888/checking'
bToSerial_URL = 'http://localhost:7777/bbb'

def assist_A():

    data = {"word": "TEST_script","code_num": 312}

    res = requests.post(assist_URL, data=json.dumps(data))
    print(res)


def serial_A():

    data = {"word": "Serial", "code_num": 112}

    res = requests.post(serial_URL, data=jsonify(data))
    print(res)

def bToSerial():

    data = {"code_num": 312}

    res = requests.post(bToSerial_URL, json=json.dumps(data))
    print(res.text)

if __name__ == "__main__":
    print("choose COMMAND")
    print("1 : assistant -> A server")
    print("2 : pyserial -> A server_renderTEMPLATE")

    cmd_num = int(input())

    if cmd_num == 1:
        assist_A()
    elif cmd_num == 2:
        serial_A()
    elif cmd_num ==3:
        bToSerial()
    else:
        print("Wrong COMMAND")
