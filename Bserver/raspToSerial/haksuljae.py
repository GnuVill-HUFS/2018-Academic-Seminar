import serial
import json
import requests
import re

A_SERVER = '192.168.1.4:3333'
COM = '/dev/ttyACM0'


def serial_connection(car_move):
    car_move_num = {306: 'b', 312: 'f', 303: 'l', 309: 'r'}
    new_car_move = car_move_num[car_move]
    print("==== ard START ======")
    ser = serial.Serial(COM, 9600)
    ser.read()
    print("==== ard 12 ======")
    ser.read(ser.write(bytes(new_car_move + ' ', encoding='ascii')))
    print("==== ard 123 ======")  # b대신에 dictionary의 key값이 들어가야한다.
    temp = ser.readline()
    print('=========Finish=====')
    temp = temp.decode('utf-8')
    temp = int(re.findall('\d+', temp)[0])
    print(temp)
    json_data = {'code_num': int(temp)}
    try:
        requests.post(A_SERVER + '/checking', json.dumps(json_data))
    except:
        return "SER"
    have_error = {'code_num': 444}
    requests.post(A_SERVER + '/checking', json.dumps(have_error))
    return "DONE"


if __name__ == "__main__":
    serial_connection(312)



