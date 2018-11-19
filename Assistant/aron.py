import requests, json
from flask import jsonify

assist_URL = 'http://192.168.1.4:3333/aaron'
#assist_URL = 'http://localhost:3333/aaron'
serial_URL = 'http://192.168.1.4:3333/checking'
#serial_URL = 'http://localhost:3333/checking'
bToSerial_URL = 'http://192.168.1.5:4444/bbb'
#bToSerial_URL = 'http://localhost:4444/bbb'

def assist_A():

    data = {"code_num": 312}
    print("AA")
    res = requests.post(assist_URL, data=json.dumps(data))
    print(res.text)


def serial_A():

    data = {"word": "Serial", "code_num": 312}

    res = requests.post(serial_URL, data=json.dumps(data))
    print(res.text)

def bToSerial():

    data = {"code_num": 312}

    requests.post(bToSerial_URL, data=json.dumps(data))
    #print(res.text)

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
