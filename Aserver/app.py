from flask import Flask,render_template, redirect, url_for
import requests, json, webbrowser
from flask import request
import os
from urllib.parse import urljoin

app = Flask(__name__, static_url_path='/static')

@app.route('/aaron', methods=['POST','GET'])
def A_rasp():
    if request.method == 'POST':
        try:
            data = json.loads(request.data)#푸는것
            res = requests.post('http://localhost:4444/bbb', data = json.dumps(data))
            return res.text
        except:
            HaveError = {'code_num': 312}
            #file_path = 'woo.html'
            #file_path = urljoin('file://'.os.path.abspath(file_path))
            return render_template('woo.html', names=HaveError)

@app.route('/checking',methods=['POST','GET'])
def Check():
    if request.method == 'POST':
        back = json.loads(request.data)
        requests.post('http://localhost:3333/save', data=json.dumps(back))
        #return render_template('woo.html', names = back)

    elif request.method == 'GET':
        data = request.args.get('code_num')
        #word = data['word']
        return webbrowser.open('http://localhost:3333/save?code_num='+str(data))

@app.route('/save', methods = ['GET','POST'])
def save():
    if request.method == 'POST':
        back = json.loads(request.data)
        requests.get('http://localhost:3333/checking', params=back)

    elif request.method=='GET':
        code_num = request.args.get('code_num')
        #return str(code_num)
        return render_template('woo.html', code_num=str(code_num))


if __name__ ==  '__main__':
    app.run(host='0.0.0.0', port='3333', debug=False)
