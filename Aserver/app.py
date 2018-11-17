from flask import Flask,render_template
import requests
import json
from flask import request

app = Flask(__name__)

@app.route('/aaron', methods=['POST'])
def A_rasp():
    try:
        data = json.loads(request.data)
        res = requests.post('http://localhost:7777/bbb', data = json.dumps(data))
        return json.dumps(data)
    except:
        HaveError = {'word':'Error!!!!', 'code_num': 312}
        return render_template('woo.html', names=HaveError)

@app.route('/checking',methods=['POST'])
def Check():
    back = request.data
    return render_template('woo.html', names=back)

if __name__ ==  '__main__':
    app.run(host='localhost',port='8888', debug=True)
