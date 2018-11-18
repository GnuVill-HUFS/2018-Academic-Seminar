import serial
import json
import requests


class Connector:

    def __init__(self):
        try:
            self.ser = serial.Serial('COM3', 9600)
        except:
            have_error = {'code_num': 444}
            requests.post('http://localhost:4444/checking', json.dumps(have_error))

    def serial_connection(self, car_move):
        try:
            self.ser.read()
            car_move_num = {306: 'b', 312: 'f', 303: 'l', 309: 'r'}
            new_car_move = car_move_num[car_move]
            self.ser.read(self.ser.write(bytes(new_car_move, encoding='ascii')))  # b대신에 dictionary의 key값이 들어가야한다.
            data = self.ser.readline()
            res = requests.post('http://;localhost:3333/cheking', json.dumps(data))
        except:
            have_error = {'code_num': 444}
            res=requests.post('http://localhost:4444/checking', json.dumps(have_error))


