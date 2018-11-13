from flask import Flask
import requests
from templates import Connector

app = Flask(__name__)

@app.route('/B_rasp ')
def B_rasp(direction_code):
    try:
        Connector.serial_connection(direction_code)
    except:
        HaveError = {'word':'Error!!!!', 'code_num': 555}
        res = requests.post('CheckingURL', HaveError)

if __name__ == '__main__':
    app.run()
